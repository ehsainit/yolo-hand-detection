import argparse
import cv2

from yoloV4 import YOLOv4

if __name__ == '__main__':

    ap = argparse.ArgumentParser()

    ap.add_argument('-v', '--video', type=str, default="test-images/PexelsVideos2784.mp4", help='Video to use')
    ap.add_argument('-o', '--output', type=str, default="test-images/output.avi", help='output path')

    ap.add_argument('-c', '--confidence', default=0.4, help='Confidence for yolo')
    args = ap.parse_args()


    yolo = YOLOv4("models/yolov4-custom.cfg", "models/yolov4-custom.weights", gpu=True)


    yolo.confidence = float(args.confidence)

    cv2.namedWindow("Hand Detector")
    cam = cv2.VideoCapture(args.video)
    out = cv2.VideoWriter(args.output, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (416, 416))

    while 1:
        r, frame = cam.read()
        if r:
            classIds, scores, boxes  = yolo.inference(frame)

            for (classId, score, box) in zip(classIds, scores, boxes):
                cv2.rectangle(frame,  (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), color=(0, 255, 0), thickness=2)

            out.write(frame)

            cv2.imshow('Hand Detector', frame)
            # Press Q on keyboard to stop recording
            if cv2.waitKey(1) & 0xFF==ord('q'):
                break
        else:
            pass

    cv2.destroyWindow("Hand Detector")
    cam.release()