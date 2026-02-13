#  Face Tracking with Python & OpenCV

A real-time **Face and Eye Tracking** project implemented in **Python** using **OpenCV** and Haar Cascade classifiers.
This project captures video from a webcam, detects faces, and then detects eyes within each detected face.

---

##  Features

* Real-time face detection using Haar Cascades
* Eye detection inside detected face regions
* Webcam video processing
* Clean and beginner-friendly code structure
* Suitable for **computer vision portfolios and resumes**

---

##  Technologies Used

* **Python 3**
* **OpenCV (cv2)**
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

## ⚙️ Installation & Setup

### 1 Clone the repository

```bash
git clone https://github.com/sagharmaktabkhah/face-tracking.git
cd face-tracking
```

### 2 Install dependencies

Make sure Python is installed, then run:

```bash
pip install opencv-python
```

### 3 Download Haar Cascade models

Make sure the following files are placed inside the `models/` directory:

* `haarcascade_frontalface_default.xml`
* `haarcascade_eye.xml`

You can download them from the official OpenCV GitHub repository.

---

##  How to Run

```bash
python face_tracking.py
```

* Press **Q** to quit the application.
* Make sure your webcam is connected and accessible.

---

##  How It Works

1. Capture frames from the webcam
2. Convert frames to grayscale
3. Detect faces using Haar Cascade classifier
4. Detect eyes within each detected face
5. Draw bounding boxes around faces and eyes
6. Display the processed video in real time

---

##  Use Case

This project is ideal for:

* Learning **Computer Vision basics**
* Understanding real-time image processing

---

## 👤 Author

**Saghar Maktabkhah**
GitHub: [https://github.com/sagharmaktabkhah](https://github.com/sagharmaktabkhah)

---

If you like this project, feel free to star the repository!
