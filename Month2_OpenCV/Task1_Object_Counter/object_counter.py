import cv2

# Load video
cap = cv2.VideoCapture("samples_data_vtest.avi")

# Create background subtractor
object_detector = cv2.createBackgroundSubtractorMOG2()

count = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    mask = object_detector.apply(frame)

    count = cv2.countNonZero(mask)

    cv2.putText(frame, "Objects: " + str(count),
                (10,50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,0,255),
                2)

    cv2.imshow("Object Counter", frame)

    # Press ESC to exit
    if cv2.waitKey(30) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()

