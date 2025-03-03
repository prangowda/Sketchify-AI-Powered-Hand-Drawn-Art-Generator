import cv2
import numpy as np

def convert_to_sketch(image_path):
    # Read the image
    img = cv2.imread(image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur
    blur = cv2.GaussianBlur(gray, (21, 21), 0)
    
    # Detect edges using the Laplacian filter
    edges = cv2.Canny(blur, threshold1=50, threshold2=150)
    
    # Invert the image
    inverted = cv2.bitwise_not(edges)
    
    # Convert back to color to match original dimensions
    sketch = cv2.cvtColor(inverted, cv2.COLOR_GRAY2BGR)
    
    return sketch

# Capture image from camera
def capture_image():
    cap = cv2.VideoCapture(0)  # 0 is for default camera

    while True:
        ret, frame = cap.read()
        cv2.imshow("Press Space to Capture", frame)

        # Press 'Space' to capture image
        if cv2.waitKey(1) & 0xFF == ord(' '):
            cv2.imwrite("captured_photo.jpg", frame)
            break

    cap.release()
    cv2.destroyAllWindows()

# Main function
def main():
    print("📸 Capturing image...")
    capture_image()
    
    print("🎨 Converting to sketch...")
    sketch = convert_to_sketch("captured_photo.jpg")

    # Show and save the sketch
    cv2.imshow("Hand-Drawn Sketch", sketch)
    cv2.imwrite("sketch_output.jpg", sketch)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
