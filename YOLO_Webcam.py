from ultralytics import YOLO
import cv2

def run_yolo_on_video(model_path, video_source, output_filename):
    cap = cv2.VideoCapture(video_source)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    output = cv2.VideoWriter(output_filename, cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width, frame_height))
    model = YOLO(model_path)

    while True:
        success, img = cap.read()
        if success:
            results = model(img)
            processed_img = results[0].plot()
            output.write(processed_img)
            cv2.imshow('YOLOv8 Live Detection', processed_img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    output.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    MODEL = "../YOLO-Weights/yolov8n.pt"
    INPUT = 0
    OUTPUT = "output_video.avi"
    run_yolo_on_video(MODEL, INPUT, OUTPUT)
