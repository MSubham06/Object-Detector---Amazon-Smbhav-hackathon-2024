from flask import Flask, render_template, Response, request, jsonify, send_file
from flask_socketio import SocketIO, emit
import cv2
from ultralytics import YOLO
from datetime import datetime
import os
import pandas as pd

app = Flask(__name__)
socketio = SocketIO(app)  # Initialize SocketIO

# Load the YOLO model
model = YOLO('model.pt')
print("Classes:", model.names)

# Define folder and file path for logs
output_folder = "detection_logs"
os.makedirs(output_folder, exist_ok=True)
output_file_path = os.path.join(output_folder, "detected_objects.txt")

# Track detected objects
detected_objects = {}
video_streaming = False  # Video streaming state

# Open a connection to the webcam
webcamera = cv2.VideoCapture(0)

# Define color mappings based on categories
color_mappings = {
    'human': (0, 255, 0),         # Green for humans
    'vehicle': (0, 0, 255),       # Red for vehicles
    'object': (255, 255, 0)       # Yellow for other objects
}

# Define categories for objects
human_classes = ['person']
vehicle_classes = ['bicycle', 'car', 'motorcycle', 'bus', 'train', 'truck', 'boat']
object_classes = ['cat', 'dog', 'chair', 'table', 'laptop']  # Add more classes as needed

# Get color based on category
def get_color(class_name):
    if class_name in human_classes:
        return color_mappings['human']
    elif class_name in vehicle_classes:
        return color_mappings['vehicle']
    else:
        return color_mappings['object']

# Generate video frames
def generate_frames():
    global video_streaming
    while video_streaming:
        success, frame = webcamera.read()
        if not success:
            break

        # Object detection on the frame
        results = model.track(frame, conf=0.8, imgsz=480)
        boxes = results[0].boxes  # Get detection boxes

        for box in boxes:
            class_id = int(box.cls)
            confidence = float(box.conf)
            class_name = model.names[class_id]
            label = f"{class_name}: {confidence:.2f}"

            # Log detection
            if class_name not in detected_objects:
                detected_objects[class_name] = True
                with open(output_file_path, "a") as file:
                    file.write(f"{datetime.now()}: Detected {class_name}\n")
                
                # Emit detection data via WebSocket for real-time updates
                detection_data = {
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'object': class_name,
                    'confidence': confidence
                }
                socketio.emit('new_detection', detection_data)

            # Bounding box coordinates
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            color = get_color(class_name)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2, cv2.LINE_AA)

        # Convert to JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Start and stop video feed
@app.route('/control', methods=['POST'])
def control_video():
    global video_streaming
    action = request.json.get('action')
    if action == 'start':
        video_streaming = True
    elif action == 'stop':
        video_streaming = False
    return jsonify({"status": "success"})

@app.route('/video_feed')
def video_feed():
    if video_streaming:
        return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return jsonify({"error": "Video feed is not active"}), 400

# Route for downloading logs
@app.route('/download_logs', methods=['GET'])
def download_logs():
    # Save the logs as an Excel file
    file_path = 'detection_logs.xlsx'
    detection_logs = pd.read_csv(output_file_path, names=['Timestamp', 'Detected Object'])
    detection_logs.to_excel(file_path, index=False)
    
    # Return the file for download
    return send_file(file_path, as_attachment=True)

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# SocketIO event handling
@socketio.on('connect')
def on_connect():
    print('Client connected')

@socketio.on('disconnect')
def on_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, debug=True)
