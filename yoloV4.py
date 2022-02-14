import cv2


class YOLOv4:

    def __init__(self, config, model, size=(416, 416), confidence=0.2, threshold=0.2, gpu=False):

        self.confidence = confidence
        self.threshold = threshold
        self.size = size

        try:
            self.model = cv2.dnn.readNetFromDarknet(config, model)
        except:
            raise "Something went wrong while reading the model or the layers"

        if gpu:
            self.model.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
            self.model.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

        self.layers = self.model.getLayerNames()
        self.layers = [self.layers[i - 1] for i in self.model.getUnconnectedOutLayers()]

    def inference(self, image):
        model = cv2.dnn_DetectionModel(self.model)
        model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True, crop=False)

        classIds, scores, boxes = model.detect(image, confThreshold=self.confidence, nmsThreshold=self.threshold)
        return classIds, scores, boxes