

```markdown
# 🦾 YOLOv8 Real-Time Object Detection

This repository contains a Python script to perform **real-time object detection** on video input (from webcam or file) using [Ultralytics YOLOv8](https://docs.ultralytics.com/) and OpenCV.

![YOLOv8 Detection Demo](https://github.com/ultralytics/assets/raw/main/yolov8/assets/banner_yolov8.png)

## 🚀 Features

- Uses [YOLOv8](https://github.com/ultralytics/ultralytics) for object detection
- Live webcam or video file input
- Real-time frame-by-frame detection
- Output saved as annotated video
- Press `q` to exit the live view

---

## 📁 Project Structure

```

.
├── yolo\_video.py           # Main script for detection
├── output\_video.avi        # Output (generated after run)
├── YOLO-Weights/
│   └── yolov8n.pt          # Pre-trained YOLOv8 model weights
└── README.md               # Project documentation

````

---

## 📦 Requirements

- Python 3.7+
- [Ultralytics](https://pypi.org/project/ultralytics/)
- [OpenCV](https://pypi.org/project/opencv-python/)

Install all dependencies with:

```bash
pip install ultralytics opencv-python
````

---

## ⚙️ Usage

### 1. Clone this repository

```bash
git clone https://github.com/yourusername/yolov8-video-detection.git
cd yolov8-video-detection
```

### 2. Place your YOLOv8 weights

Place your `.pt` model file (e.g., `yolov8n.pt`) inside the `YOLO-Weights/` directory. You can download official weights from [Ultralytics YOLOv8 Releases](https://github.com/ultralytics/ultralytics/releases).

### 3. Run the script

#### For Webcam Input

```bash
python yolo_video.py
```

#### For Video File Input

Update the `INPUT` variable in the script:

```python
INPUT = "input_video.mp4"
```

---

## 📝 Script Overview

```python
model = YOLO(model_path)                # Load YOLOv8 model
results = model(img)                    # Perform detection
processed_img = results[0].plot()       # Draw bounding boxes
```

* `cv2.VideoCapture(0)` – reads webcam (change `0` to filename for video input)
* `cv2.imshow()` – displays live annotated feed
* `cv2.VideoWriter()` – saves annotated output to a file

---

## 📌 Notes

* Press **`q`** to quit the live display window.
* Default video output is saved as `output_video.avi`.

---

## 🧠 Credits

* [Ultralytics](https://github.com/ultralytics/ultralytics) for the YOLOv8 models
* [OpenCV](https://opencv.org/) for video handling

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

```

Let me know if you want to add a demo video/gif, requirements.txt, or GitHub Actions for auto-testing!
```
