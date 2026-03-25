# Hand Air Writing System (Virtual Canvas)
##  Overview

This project is a **real-time Air Writing system** that allows users to write in the air using their fingers.
The system tracks hand movements through the webcam and converts them into drawing on the screen.

It is built using **Computer Vision techniques** and demonstrates real-time interaction between human gestures and digital systems.

---

##  Features

*  Real-time camera input
*  Hand tracking using MediaPipe
*  Finger position detection (Index finger)
*  Air drawing (Virtual Canvas)
*  Gesture control:

  * ☝️ One finger → Draw
  * ✌️ Two fingers → Stop drawing
  * ✊ Closed hand → Clear canvas

---

##  How It Works

1. The webcam captures live video frames
2. Hand landmarks are detected
3. The index finger position is extracted
4. The system connects points to simulate drawing
5. Gestures control the drawing behavior

---

##  Tech Stack

* Python
* OpenCV
* MediaPipe
* NumPy

---

##  Challenges & Solutions

###  Camera Handling

**Problem:** Camera was not closing properly
**Solution:** Used `cap.release()` and `cv2.destroyAllWindows()`

---

###  MediaPipe Setup

**Problem:** `module 'mediapipe' has no attribute 'solutions'`
**Solution:** Reinstalled a stable version and fixed environment conflicts

---

###  Coordinate Misalignment

**Problem:** Hand landmarks appeared in the opposite direction
**Solution:** Applied proper image flipping before processing

---

###  Drawing Instability

**Problem:** Lines were broken or not continuous
**Solution:** Stored previous coordinates and connected them smoothly

---

###  Continuous Drawing Issue

**Problem:** The system was always drawing
**Solution:** Implemented gesture-based control using finger states

---

##  Demo

![Screenshot 2026-03-25 161349](https://github.com/user-attachments/assets/3805d2f6-11d9-4cbb-a1c1-edd11653482b)


##  How to Run

### 1. Install dependencies

```bash
pip install opencv-python mediapipe numpy
```

### 2. Run the script

```bash
python your_file_name.py
```

---

## 📌 Project Structure

```
Air-Writing/
│
├── main.py
├── README.md
└── requirements.txt (optional)
```

---

##  Future Work (AI Integration)

*  Handwriting recognition (convert drawing to text)
*  Smoother drawing using interpolation
*  Color selection & UI improvements
*  Mobile/web integration

---

##  Learning Outcomes

This project helped in understanding:

* Real-time computer vision
* Hand tracking systems
* Human-computer interaction
* Debugging and problem solving

---

Developed by Anwaar Mabrouk 💙
