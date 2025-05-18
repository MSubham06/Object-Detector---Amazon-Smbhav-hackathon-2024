# Progect aka Pro-(gect) 🚀  
*A Team Project for **Amazon Smbhav Hackathon 2024***

This project, **Progect**, is a real-time object detection web application built for dynamic video streaming, object detection, and interactive user experiences. It allows users to stream live video, detect objects in real-time, and download detection logs—with customizable settings for enhanced control.

> 🔗 **Video Demo**: [Google Drive](https://drive.google.com/file/d/1m2-TNuCpCgIBHtPGb2XKbCFhOzDEDZHD/view?usp=sharing)  
> ▶️ **YouTube Link**: [Watch on YouTube](https://youtu.be/h-ACxbLcYLI)

![Object Detection Demo](https://github.com/user-attachments/assets/3f3ebd8c-1b58-4158-bf25-41dc623537e3)

---

## 💻 Tech Stack

- **HTML** – UI layout for video, controls, and detection display  
- **JavaScript** – Frontend interactivity and real-time updates  
- **Python** – Backend logic, object detection, and video processing  
- **Flask** – Lightweight backend framework  
- **Flask-SocketIO** – Real-time communication between frontend and backend  
- **OpenCV** – Captures and processes video frames  
- **YOLO** – Object detection model for bounding boxes  
- **Pandas** – Logs detection data and exports it to Excel/JSON  
- **Socket.IO** – Live communication for seamless video updates

![Screenshot](https://github.com/user-attachments/assets/b351d2b9-e0e8-4bc2-bfda-f570fe5506fb)

---

## 🌟 Features

1. **Live Video Streaming** in browser  
2. **Real-Time Object Detection** with bounding boxes  
3. **Adjustable Detection Settings** (threshold, frequency)  
4. **Downloadable Logs** in JSON with timestamp, object type, confidence  
5. **Interactive Dashboard** for statistics and history  
6. **Differentiated Detection** of persons vs. vehicles (color-coded)

![Live Detection](https://github.com/user-attachments/assets/5d2791d1-1c34-43d1-bd97-48a1efb829d0)

---

## 🔮 Future Enhancements

- 🔧 Custom YOLO model support (user training)
- 🎥 Multi-Camera streaming
- 📱 Mobile app integration
- 🚨 Automated alerts for detected events
- 📊 Detection analytics and heatmaps

---

## 🔁 Data Flow Diagram

![Data Flow](https://github.com/user-attachments/assets/0a89f3f5-7f07-4edf-a4eb-d3aea1ed40cc)

---

## 🌍 Use Cases

- 🛡️ Security & Surveillance  
- 🛒 Retail Analytics  
- 🚦 Smart Cities  
- 🏥 Healthcare Monitoring  
- 🌾 Agriculture Drones  
- 📚 Education & Research  

---

## 🎯 Object Detection Classes (YOLO Model)

Using a pre-trained `model.pt`, capable of detecting 80+ object classes such as:

- person, car, bicycle, bus, dog, cat, chair, cell phone, laptop, etc.  
*(Full class list in source code.)*

---

## ⚙️ How It Works

Each frame from the live video stream is passed through the YOLO model which returns predictions (bounding box, label, confidence score). These are then rendered on the UI in real-time and stored in structured logs.

---

## 🧑‍💻 Installation

```bash
# Clone the repository
git clone https://github.com/username/progect.git
cd progect

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Visit the app in browser
http://127.0.0.1:5000
```

---

## 🤝 Contribution Guidelines

We welcome contributions from developers, enthusiasts, and open-source lovers.

```bash
# Fork the repo
# Create a new branch
git checkout -b feature-name

# Make your changes
# Commit your work
git commit -m "Added feature X"

# Push your branch
git push origin feature-name

# Open a pull request 🚀
```

---

## 🙌 Acknowledgements

> This is a collaborative team effort built as part of the **Amazon Smbhav Hackathon 2024**.  
> Special thanks to the mentors, reviewers, and our peers who contributed to making Progect a success.  
> Stay tuned for more updates and version upgrades!

---

Thank you for exploring **Progect** – where innovation meets real-time intelligence! 🌐🧠
