import cv2
import glob

from yoloV4 import YOLOv4

image_list = []
labeled_dir = "test-images/labeled/"

if __name__ == '__main__':
    yolo = YOLOv4("models/yolov4-custom.cfg", "models/yolov4-custom.weights", gpu=False)
    c  = 0

    for filename in glob.glob('test-images/*.jpg'): #assuming gif
        im= cv2.imread(filename)

        classIds, scores, boxes = yolo.inference(im)
        for (classId, score, box) in zip(classIds, scores, boxes):
            cv2.rectangle(im, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), color=(0, 255, 0), thickness=2)
            text = '%s: %.2f' % ("hand", score)
            cv2.putText(im, text, (box[0], box[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 1,
                color=(0, 255, 0), thickness=2)

        cv2.imwrite(labeled_dir + "image" + str(c) + ".jpg", im)
        c+=1
