import cv2


def main():
    # Initialize camera
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Error: Camera could not be opened")
        return

    # Load Haar Cascade models
    face_model = cv2.CascadeClassifier(
        "models/haarcascade_frontalface_default.xml"
    )
    eye_model = cv2.CascadeClassifier(
        "models/haarcascade_eye.xml"
    )

    while True:
        ret, img = cam.read()
        if not ret:
            print("Failed to grab frame")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_model.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5
        )

        img_out = img.copy()

        if len(faces) > 0:
            x, y, w, h = faces[0]
            x2, y2 = x + w, y + h

            cv2.rectangle(img_out, (x, y), (x2, y2), (0, 255, 0), 3)

            gray_face = gray[y:y2, x:x2]

            eyes = eye_model.detectMultiScale(
                gray_face,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )

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

        cv2.imshow("Face Tracking", img_out)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
