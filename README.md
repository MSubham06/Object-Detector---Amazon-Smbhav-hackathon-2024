# Pro-(gect)  

This project, **Progect**, is a real-time object detection web application designed for dynamic video streaming, object detection, and user interactivity. It allows users to stream live video, detect objects in real-time, and download detection logs with customizable detection settings.

## video link : https://drive.google.com/file/d/1kb_AU5jfYz4YmRZbpKbb4_xNtrJBpP2p/view?usp=drive_link

## (progect) Youtube video link : https://youtu.be/h-ACxbLcYLI


![obj](https://github.com/user-attachments/assets/3f3ebd8c-1b58-4158-bf25-41dc623537e3)


## Tech Stack

The following technologies are used in this project:

- **HTML**: Structures the layout for video display, object detection details, and user controls.
- **JavaScript**: Adds interactivity, enabling real-time video updates, detection settings adjustments, and log downloads.
- **Python**: Manages backend operations, video processing, and object detection using image processing libraries.
- **Flask**: Serves as the backend framework, handling HTTP requests and data flow.
- **Flask-SocketIO**: Enables real-time, bidirectional communication between frontend and backend for smooth video feed updates.
- **OpenCV**: Used in Python for real-time video frame capture, manipulation, and transformation.
- **YOLO (You Only Look Once)**: Detects objects in real-time on video frames, drawing bounding boxes and labels.
- **Pandas**: Organizes detection data into an Excel format for creating downloadable logs with metadata.
- **Socket.IO**: Ensures seamless data flow between server and client for live video stream updates.

![WhatsApp Image 2024-11-14 at 03 47 33_6cc0ad72](https://github.com/user-attachments/assets/b351d2b9-e0e8-4bc2-bfda-f570fe5506fb)

## Features

1. **Live Video Streaming**: Stream live video directly within the web browser.
2. **Real-Time Object Detection**: Apply object detection on live video feeds with bounding boxes.
3. **Detection Settings**: Adjust detection parameters, including threshold and frequency.
4. **Downloadable Logs**: Export detection logs in JSON format, capturing details like object type, confidence level, and timestamp.
5. **Dashboard**: View current and historical detections, logs, and statistical insights.
6. **Differentiated Object Detection**: Detect different object types—**persons** and **vehicles**—with unique bounding box colors for better visual distinction.

![image](https://github.com/user-attachments/assets/5d2791d1-1c34-43d1-bd97-48a1efb829d0)

## Future Enhancements

1. **Model Customization**: Allow users to train and deploy custom object detection models.
2. **Multi-Camera Support**: Stream and detect objects from multiple video sources simultaneously.
3. **Mobile App Integration**: Extend detection functionality to mobile platforms.
4. **Automated Alerts**: Set detection triggers to notify users in real-time for specific object detections.
5. **Advanced Analytics**: Provide insights based on detection history, heatmaps, and trends analysis.

## Data Flow Diagram
![diagram-export-11-14-2024-11_10_35-AM](https://github.com/user-attachments/assets/0a89f3f5-7f07-4edf-a4eb-d3aea1ed40cc)


## Potential Use Cases

Upon completion, **Progect** will be valuable across various domains:

1. **Security & Surveillance**: Automatically identify suspicious activities or unauthorized access.
2. **Retail Analytics**: Track customer behavior to optimize store layout and marketing efforts.
3. **Smart City Applications**: Monitor and manage traffic conditions in real-time.
4. **Healthcare & Assisted Living**: Observe patient movements and notify caregivers for enhanced care.
5. **Agriculture**: Monitor crop and livestock conditions using drone-based detection systems.
6. **Education & Research**: A practical tool for students and researchers exploring object detection.

## Object Detection Model

This project utilizes a pre-trained YOLO (You Only Look Once) model to detect a variety of objects in real-time from the video feed. The model (`model.pt`) is capable of detecting the following classes:

- **0**: person
- **1**: bicycle
- **2**: car
- **3**: motorcycle
- **4**: airplane
- **5**: bus
- **6**: train
- **7**: truck
- **8**: boat
- **9**: traffic light
- **10**: fire hydrant
- **11**: stop sign
- **12**: parking meter
- **13**: bench
- **14**: bird
- **15**: cat
- **16**: dog
- **17**: horse
- **18**: sheep
- **19**: cow
- **20**: elephant
- **21**: bear
- **22**: zebra
- **23**: giraffe
- **24**: backpack
- **25**: umbrella
- **26**: handbag
- **27**: tie
- **28**: suitcase
- **29**: frisbee
- **30**: skis
- **31**: snowboard
- **32**: sports ball
- **33**: kite
- **34**: baseball bat
- **35**: baseball glove
- **36**: skateboard
- **37**: surfboard
- **38**: tennis racket
- **39**: bottle
- **40**: wine glass
- **41**: cup
- **42**: fork
- **43**: knife
- **44**: spoon
- **45**: bowl
- **46**: banana
- **47**: apple
- **48**: sandwich
- **49**: orange
- **50**: broccoli
- **51**: carrot
- **52**: hot dog
- **53**: pizza
- **54**: donut
- **55**: cake
- **56**: chair
- **57**: couch
- **58**: potted plant
- **59**: bed
- **60**: dining table
- **61**: toilet
- **62**: tv
- **63**: laptop
- **64**: mouse
- **65**: remote
- **66**: keyboard
- **67**: cell phone
- **68**: microwave
- **69**: oven
- **70**: toaster
- **71**: sink
- **72**: refrigerator
- **73**: book
- **74**: clock
- **75**: vase
- **76**: scissors
- **77**: teddy bear
- **78**: hair drier
- **79**: toothbrush


### How It Works
The `model.pt` file contains a YOLO-based object detection model that identifies the above classes in real-time video feeds. The model works by drawing bounding boxes around each detected object and labeling them with the corresponding class name. This is achieved by processing the video frames through the model, which predicts the class labels and confidence scores for each detected object.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/progect.git
   cd progect
   pip install -r requirements.txt
   python app.py
Navigate to the project directory:

cd progect
## Install the required dependencies:

pip install -r requirements.txt
Start the application:

python app.py
Open your browser and go to http://127.0.0.1:5000 to view the application.

## Contributing
Contributions are welcome! Please follow these steps:


## Fork the repository.
Create a new branch for your feature:

git checkout -b feature-name
Commit your changes:


git commit -m "Add new feature"

## Push your branch:

git push origin feature-name
Submit a pull request for review.
Thank you for exploring Progect! We look forward to seeing how it inspires new use cases and advancements in real-time object detection.
