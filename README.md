# YoloV4 Hand Detector

Pre-trained Hand Detector based-on YOLOv4 architecture.

## Description

There are couple pre-trained hand detectors in the wild. Most of them based on MobileNetSSD networks and other are based on YOLO architecture. Since, the majority of YOLO-based hand detectors lack proper documentation, it is challanging to re-train them.

The goals of this project is to offer a stable hand detector with a proper documentation making it easier fo them to fine-tune for their own object(hand) detection tasks.

## Dataset

The Model was trained on custom [EgoHands](http://vision.soic.indiana.edu/projects/egohands/) dataset mainly.

EgoHands is basically meant for detecting complex egocentric hands interactions, i.e each interaction is a class.

My goal is to detect the hand as an object from egocentric/pseudo-egocentric point-of-view.

An annotated version of Egohand dataset is available for 4 activity detection [Roboflow EgoHands](https://public.roboflow.com/object-detection/hands/1)
For the task of hand/no-hand, a modification of the annotation files was required. Instead of having 4 class, only one is needed for all hand instances across all images.
The training set consists of 90% of the total images number.

### Training

In order to train YOLOv4, the [DarkNet](https://github.com/AlexeyAB/darknet) by Alexey Bochkovskiy was used and the instructions as specified in the docs were followed.

Information about the training parameters you can find in the custom-yolov4 configuration file under the models directory.

The model was trained until there was no significant change in the average loss value (ca. 12k iterations). mAP of ~95% was achieved.

![plot](images/yolotraining.png)


## License

This project is licensed under the [MIT License] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [cansik/yolo-hand-detection](https://github.com/cansik/yolo-hand-detection)
* [Handtracking](https://github.com/victordibia/handtracking)
