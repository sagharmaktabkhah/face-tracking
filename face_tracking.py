import cv2
import pyautogui as robot

robot.FAILSAFE = False  # Prevent sudden crash if mouse goes to corner


def main():
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Error: Camera could not be opened")
        return

    face_model = cv2.CascadeClassifier(
        "models/haarcascade_frontalface_default.xml"
    )

    screen_w, screen_h = robot.size()

    while True:
        ret, img = cam.read()
        if not ret:
            print("Failed to grab frame")
            break

        img = cv2.flip(img, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_model.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5
        )

        img_out = img.copy()

        if len(faces) > 0:
            x, y, w, h = faces[0]

            # Draw face rectangle
            cv2.rectangle(img_out, (x, y), (x + w, y + h), (0, 255, 0), 3)

            # Get face center
            face_center_x = x + w // 2
            face_center_y = y + h // 2

            # Get frame size
            frame_h, frame_w, _ = img.shape

            # Map face position to screen size
            mapped_x = int(face_center_x / frame_w * screen_w)
            mapped_y = int(face_center_y / frame_h * screen_h)

            # Move mouse
            robot.moveTo(mapped_x, mapped_y)

            # Show center point
            cv2.circle(img_out, (face_center_x, face_center_y), 5, (0, 0, 255), -1)

        cv2.imshow("Head Controlled Mouse", img_out)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
