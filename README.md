#  Head-Controlled Mouse using Face Tracking (Python & OpenCV)

A real-time **Head-Controlled Mouse Automation System** built with **Python**, **OpenCV**, and **PyAutoGUI**.
This project detects the user's face through a webcam and maps head movement to control the system mouse cursor.

---

##  Features

*  Real-time face detection using Haar Cascades
*  Head-controlled mouse movement
*  Live webcam processing
*  Face position mapped to full screen resolution
*  Clean and modular Python structure
*  Portfolio-ready computer vision project

---

##  Technologies Used

* **Python 3**
* **OpenCV (cv2)**
* **PyAutoGUI**
* Haar Cascade Classifiers

---

##  Project Structure

```
face-tracking/
│── face_tracking.py
│── models/
│   ├── haarcascade_frontalface_default.xml
│   └── haarcascade_eye.xml
│── README.md
```

---

##  Installation & Setup

### 1 Clone the repository

```bash
git clone https://github.com/sagharmaktabkhah/face-tracking.git
cd face-tracking
```

### 2 Install dependencies

```bash
pip install opencv-python pyautogui
```

### 3 Make sure Haar Cascade models exist

Place the following files inside the `models/` folder:

* `haarcascade_frontalface_default.xml`
* `haarcascade_eye.xml`

You can download them from the official OpenCV GitHub repository.

---

##  How to Run

```bash
python face_tracking.py
```

* Move your head to control the mouse cursor
* Press **Q** to exit the application
* Ensure your webcam is accessible

---

##  How It Works

1. Capture video frames from webcam
2. Detect face using Haar Cascade
3. Compute the center of the detected face
4. Map face coordinates to screen resolution
5. Move mouse cursor using PyAutoGUI
6. Display processed video with visual tracking

---

##  Use Cases

* Learning real-time computer vision
* Understanding coordinate mapping
* Human-computer interaction experiments
* Assistive technology prototypes
* Portfolio and resume enhancement

---

##  Future Improvements

* Smooth cursor movement (motion filtering)
* Sensitivity control settings
* Eye-blink detection for mouse click
* Scroll control using head tilt
* Replace Haar Cascade with MediaPipe or deep learning model

---

##  Author

**Saghar Maktabkhah**
GitHub: [https://github.com/sagharmaktabkhah](https://github.com/sagharmaktabkhah)

---

⭐ If you found this project interesting, consider giving it a star!
