import cv2
import torch

# Load a pre-trained YOLOv5 model (you can use any YOLOv5 model from the repository)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Initialize the video stream
cap = cv2.VideoCapture(0)  # Change to video file path if needed

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Perform detection
    results = model(frame)

    # Render results on the frame
    frame = results.render()[0]

    # Display the resulting frame
    cv2.imshow("Object Detection", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
