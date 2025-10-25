# 🛒 AI Smart Checkout System

## Overview
The **AI Smart Checkout System** is an intelligent, AI-driven retail automation solution designed to streamline in-store checkout operations using computer vision, IoT, and machine learning.  
It integrates **YOLOv8**, **DeepSORT**, **RFID**, and **weight sensors** to create a fully automated, contactless checkout experience that reduces human intervention while improving speed, accuracy, and customer satisfaction.

---

## 🚀 Key Features
- **Real-time Object Detection & Tracking:** YOLOv8 + DeepSORT integration for multi-object recognition and tracking.  
- **Smart Conveyor Automation:** Automated item scanning and conveyor control through Arduino serial communication.  
- **RFID & Weight Validation:** Dual-verification mechanism to ensure item integrity and prevent checkout errors.  
- **WebSocket IoT Communication:** Low-latency bidirectional communication between POS, RFID, camera, and scan tunnel systems.  
- **POS Interface (ReactJS):** Dynamic, user-friendly dashboard for transaction monitoring and billing.  
- **Edge AI Integration:** Runs efficiently on embedded devices like Raspberry Pi and Jetson Nano for real-time inference.

---

## 🧠 System Architecture
The project follows a modular and event-driven architecture with **three main layers**:

| Layer | Description |
|--------|--------------|
| **Perception Layer** | Handles object detection, tracking, and sensor data acquisition from cameras and IoT devices. |
| **Processing Layer** | Uses AI models (YOLOv8, DeepSORT) and validation logic to confirm object identity and consistency. |
| **Application Layer** | Displays processed data, manages billing, and synchronizes transactions via WebSocket channels. |

---

## ⚙️ Tech Stack
| Component | Technology |
|------------|-------------|
| **AI/ML** | YOLOv8, DeepSORT, OpenCV |
| **Backend** | Python (AsyncIO, WebSocket, Serial) |
| **Frontend (POS)** | ReactJS, Material UI |
| **IoT Devices** | Arduino, RFID Reader, Android (OpenCV) |
| **Edge Deployment** | Raspberry Pi, Jetson Nano |

---

## 🧩 Workflow Summary
1. Object is detected by the **YOLOv8 model**.  
2. **DeepSORT** tracks the object with a unique ID across frames.  
3. Detected item metadata is sent to the **RFID validation unit**.  
4. **Weight sensors** verify item accuracy.  
5. **POS interface** finalizes the checkout process and generates receipts.  

---

## 📊 Outcomes
- ⏱️ Reduced average checkout time by **60%**.  
- 🎯 Achieved **95%+ detection accuracy** under real conditions.  
- 🔄 Ensured **real-time synchronization** across IoT devices and POS.  
- 🧠 Delivered a **fully automated checkout** with zero manual dependencies.

---

## 🧰 Folder Structure
```
AI-Smart-Checkout-System/
├── README.md
├── Technical_Approach_AI_Smart_Checkout_v3.pdf
├── architecture_diagram.png
├── workflow_diagram.png
├── system_components_overview.png
├── src/
│   ├── video_processing.py
│   ├── scan_tunnel_interface.py
│   └── pos_checkout_interface.js
└── assets/
    └── demo_videos, references, and UI mockups
```

---

## 🏗️ Deployment
To run the AI Smart Checkout modules locally:
```bash
pip install -r requirements.txt
python src/video_processing.py
```
Frontend POS Interface (React):
```bash
cd pos_interface
npm install
npm start
```

---

## 🧾 Documentation
Full technical explanation and system details are available in the attached PDF:  
📄 [Technical_Approach_AI_Smart_Checkout_v3.pdf](./Technical_Approach_AI_Smart_Checkout_v3.pdf)

---

## 💡 Future Enhancements
- Integration with **Edge TPU / NVIDIA Jetson** for on-device inference.  
- **Cloud-based analytics** for operational performance tracking.  
- Integration with **payment gateways** and **inventory management systems**.  

---

**Confidential – For Research & Academic Portfolio Use Only**  
