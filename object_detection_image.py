import cv2
import torch

# Load a pre-trained YOLOv5 model (you can use any YOLOv5 model from the repository)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Load the image
image_path = 'image.jpeg'  # Replace with the path to your image
image = cv2.imread(image_path)

# Perform detection
results = model(image)

# Render results on the image
image = results.render()[0]

# Resize the image (for example, to 800x600)
new_width = 800
new_height = 600
resized_image = cv2.resize(image, (new_width, new_height))

# Display the resulting image
cv2.imshow("Object Detection", resized_image)
cv2.waitKey(0)  # Wait for a key press to close the window

# Save the resulting image (optional)
cv2.imwrite('output_image.jpg', resized_image)

# Close the OpenCV window
cv2.destroyAllWindows()
