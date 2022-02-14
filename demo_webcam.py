import argparse
import cv2

from yoloV4 import YOLOv4

if __name__ == '__main__':

    ap = argparse.ArgumentParser()

    ap.add_argument('-d', '--device', type=int, default=0, help='Device to use')
    ap.add_argument('-s', '--image_size', default=416, help='Size for yolo')
    ap.add_argument('-c', '--confidence', default=0.2, help='Confidence for yolo')
    args = ap.parse_args()


    yolo = YOLOv4("models/yolov4-custom.cfg", "models/yolov4-custom.weights", gpu=True)


    yolo.size = int(args.image_size)
    yolo.confidence = float(args.confidence)

    print("Starting webcam...")
    cv2.namedWindow("Hand Detector")
    cam = cv2.VideoCapture(args.device)

    while 1:
        r, frame = cam.read()

        if r:

            classIds, scores, boxes  = yolo.inference(frame)

            for (classId, score, box) in zip(classIds, scores, boxes):
                cv2.rectangle(frame,  (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), color=(0, 255, 0), thickness=2)

            cv2.imshow("Hand Detector", frame)

            key = cv2.waitKey(20)
            if key == 27:  # exit on ESC
                break
        else:
            break

    cv2.destroyWindow("Hand Detector")
    cam.release()