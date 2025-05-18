from flask import request, jsonify, send_file
import pandas as pd
from datetime import datetime

# Initialize an empty DataFrame to store detection logs
columns = ['Timestamp', 'Object Type', 'Speed (km/h)', 'Location', 'Confidence']
detection_logs = pd.DataFrame(columns=columns)

# Function to add detection data
def add_detection_log(object_type, speed, location, confidence):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    detection_logs.loc[len(detection_logs)] = [timestamp, object_type, speed, location, confidence]

# Route for logging detection data
def log_detection():
    data = request.get_json()
    object_type = data.get('object_type')
    speed = data.get('speed')
    location = data.get('location')
    confidence = data.get('confidence')

    # Add the received detection data to the log
    add_detection_log(object_type, speed, location, confidence)
    
    return jsonify({'status': 'success'}), 200

# Route for downloading logs
def download_logs():
    # Save the logs as an Excel file
    file_path = 'detection_logs.xlsx'
    detection_logs.to_excel(file_path, index=False)
    
    # Return the file for download
    return send_file(file_path, as_attachment=True)
