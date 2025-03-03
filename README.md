# **Sketchify: AI-Powered Hand-Drawn Art Generator** 🎨  

## **📌 Description**  
**Sketchify** is a Python-based tool that converts **camera-captured images** into **hand-drawn sketches** using **OpenCV**. The program applies edge detection and image processing techniques to transform real-world images into artistic pencil sketches.  


Python tool that converts camera-captured images into hand-drawn sketches using OpenCV. The process involves edge detection and image processing techniques to mimic a pencil sketch effect.

---
## **🛠 Steps to Convert an Image to Hand-Drawn Art**
1. Capture an Image from the Camera
2. Convert it to Grayscale
3. Apply Gaussian Blur to smoothen the image
4. Perform Edge Detection using the Laplacian filter
5. Invert & Blend the Image to create a realistic sketch effect

---

## **🚀 Features**  
✅ **Capture image from webcam** 📸  
✅ **Convert image into a hand-drawn sketch** ✏️  
✅ **Applies Gaussian blur & edge detection for realism**  
✅ **Saves the final sketch as an output image** 🖼️  
✅ **Easy-to-use interface**  

---

## **🛠 Technologies Used**  
- **Python** 🐍  
- **OpenCV** (Image Processing)  
- **NumPy** (Array Manipulation)  

---

## **📂 Project Structure**  
```
📦 Sketchify
 ┣ 📜 sketchify.py          # Main Python script
 ┣ 📜 requirements.txt      # Dependencies list
 ┣ 📜 README.md             # Documentation
 ┗ 📂 output/               # Folder for generated sketches
```

---

## **🔧 Installation & Setup**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/pranagowda/Sketchify.git
cd Sketchify
```

### **2️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Application**  
```bash
python sketchify.py
```

---

## **📜 How It Works**  

1️⃣ **Launch the script** – Your webcam opens automatically.  
2️⃣ **Press "Space"** – Capture an image from your camera.  
3️⃣ **Sketchify processes the image** – Applies grayscale, blur, and edge detection.  
4️⃣ **The hand-drawn sketch appears** – It is displayed and saved as `sketch_output.jpg`.  

---

## **🔗 API Endpoints (For Future Enhancements)**  
| **Method** | **Endpoint**       | **Description**                  |  
|------------|--------------------|----------------------------------|  
| `POST`     | `/upload`          | Upload an image to be sketched  |  
| `GET`      | `/download`        | Download the processed sketch   |  

---

## **📦 Requirements**  
Ensure you have **Python 3.7+** installed. Then install dependencies using:  
```bash
pip install opencv-python numpy
```

---

## **🎯 Future Enhancements**  
✅ **Live Sketch Mode** – Apply the effect in real-time.  
✅ **GUI Interface** – Add a graphical interface using Tkinter/PyQt.  
✅ **Color Sketching** – Generate colored artistic sketches.  
✅ **Batch Processing** – Convert multiple images at once.  

