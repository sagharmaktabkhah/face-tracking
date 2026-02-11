# %%
import cv2


# Initialize camera

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Error: Camera could not be opened")
    exit()

# %%
# Load Haar Cascade models

face_model = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_model = cv2.CascadeClassifier("haarcascade_eye.xml")

# %%
# Main loop

while True:
    ret, img = cam.read()  # Read frame from camera
    if not ret:
        print("Failed to grab frame")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_model.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    # If no face is detected, just show the frame
    if len(faces) == 0:
        cv2.imshow("Face Tracking", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        continue

    # Use the first detected face
    x, y, w, h = faces[0]
    x2, y2 = x + w, y + h

    # Draw face rectangle
    img_out = img.copy()
    cv2.rectangle(img_out, (x, y), (x2, y2), (0, 255, 0), 3)

    # Extract face region for eye detection
    gray_face = gray[y:y2, x:x2]

    # Detect eyes inside the face region
    eyes = eye_model.detectMultiScale(
        gray_face,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw rectangles around detected eyes (max 2 eyes)
    for i, (ex, ey, ew, eh) in enumerate(eyes):
        cv2.rectangle(
            img_out,
            (x + ex, y + ey),
            (x + ex + ew, y + ey + eh),
            (0, 0, 255),
            2
        )
        if i == 1:
            break

    # Show result
    cv2.imshow("Face Tracking", img_out)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources

cam.release()
cv2.destroyAllWindows()


