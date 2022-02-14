# YoloV4 Hand Detector 

Pre-trained Hand Detector based-on YOLOv4 neural network.

## Description

There are already existing pre-trained hand detector in the wild, most of them based on MobileNetSSD networks and some 
of them are based on Yolo neural network architecture. However, the vast majority(yolo-based) do not include information about the 
implementation used to train, thus making it harder to fine-tune/transfer-learning.

Hence, the goals of this model are:
- To offer stable hand detector.
- To give others the ability to fine-tune or transfer learning and hopefully save them time :)


## Dataset 

Yolov4 was trained on custom [EgoHand](http://vision.soic.indiana.edu/projects/egohands/) dataset mainly.

This dataset was basically meant for detecting complex egocentric hands interactions, i.e each interaction is a class.
Nevertheless, my main purpose was detecting the hand as an object from egocentric/pseudo-egocentric point-of-view,
so I used a labeled Egohand dataset [Roboflow EgoHand](https://public.roboflow.com/object-detection/hands/1) and modified
the Ids in annotation files (text files) to be suitable for only one class. (just one Id - 0). In addition, I splitted
the data into train/validation sets (90% , 10%).

### Training

In order to train YOLOv4, the [DarkNet](https://github.com/AlexeyAB/darknet) by Alexey Bochkovskiy was built and the
instructions as specified in the docs were followed.

Information about the training parameters you can find in the custom-yolov4 configuration file.

The training went on for ca. 24 hours (ca. 12k iterations) on a single Tesla V100( on Colab).

![alt text](test-images/yolotraining.png)

## License

This project is licensed under the [MIT License] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [cansik/yolo-hand-detection](https://github.com/cansik/yolo-hand-detection)
* [Handtracking](https://github.com/victordibia/handtracking)
