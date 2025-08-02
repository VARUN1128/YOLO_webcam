YOLOv8 Live Video Object Detection
This script uses the YOLOv8 model to perform real-time object detection on a video feed from a webcam or a video file. It displays the processed video stream with bounding boxes around detected objects and saves the output to an .avi video file.

Requirements
Before running the script, you need to install the necessary Python libraries. You can install them using pip:

pip install ultralytics opencv-python

You will also need the YOLOv8 model weights file (.pt). The script is configured to use yolov8n.pt, which will be downloaded automatically by the ultralytics library if it's not found locally.

How to Run
Save the Code: Save the Python code as a file (e.g., detect_video.py).

Organize Files: Make sure your folder structure matches the paths in the script, or update the paths accordingly. The script expects a YOLO-Weights folder.

/your_project_folder
|-- /YOLO-Weights
|   |-- yolov8n.pt
|-- detect_video.py

Execute from Terminal: Open a terminal or command prompt, navigate to your project folder, and run the script:

python detect_video.py

View Output:

A window titled "YOLOv8 Live Detection" will appear, showing the live video feed with detections.

Press the 'q' key to stop the script.

An output_video.avi file will be saved in your project directory.

Customization
You can easily change the input and output by modifying these lines at the bottom of the script:

MODEL: Change the path to use a different YOLOv8 model (e.g., yolov8s.pt for the small model).

INPUT: Set to 0 for your primary webcam. To use a video file, change it to the file path (e.g., "path/to/my_video.mp4").

OUTPUT: Change the filename for the saved video (e.g., "my_detection.avi").

Code Explanation
The script is organized into a single function, run_yolo_on_video, for modularity and ease of use.

Initialization:

cv2.VideoCapture(video_source): Initializes the video capture from either a webcam (0) or a video file.

cv2.VideoWriter(...): Creates a video writer object to save the processed frames into an .avi file.

YOLO(model_path): Loads the specified pre-trained YOLOv8 model.

Main Loop (while True):

cap.read(): Reads one frame at a time from the video source.

model(img): Passes the current frame to the YOLO model for object detection.

results[0].plot(): Takes the detection results (bounding boxes, labels, confidence scores) and draws them onto the original frame.

output.write(processed_img): Writes the frame with the detections to the output video file.

cv2.imshow(...): Displays the processed frame in a window.

cv2.waitKey(1): Waits for a key press. The loop breaks if the 'q' key is pressed.

Cleanup:

cap.release(): Releases the video capture device.

output.release(): Finalizes and saves the output video file.

cv2.destroyAllWindows(): Closes all OpenCV windows.
