import cv2
import os

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Get the current working directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Image file name (assuming 'shad.jpg' is in the same directory as the script)
image_path = os.path.join(script_dir, 'shad.jpg')

# Load the image
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print(f"Error: Could not load image {image_path}")
    exit()

# Convert the image to grayscale as the face detector expects gray images
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the resulting image
cv2.imshow('Face Detection', image)

# Wait for a key press and close the image window
cv2.waitKey(0)
cv2.destroyAllWindows()
