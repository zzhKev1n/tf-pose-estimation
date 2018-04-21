# Software and Machine Learning Project: Dectect "Hailing a cab" motion.
<!-- 
'Openpose' for human pose estimation have been implemented using Tensorflow. It also provides several variants that have made some changes to the network structure for **real-time processing on the CPU or low-power embedded devices.** -->

## Task
You have to implement a system which, given a video stream from you webcam, detect a person who is hailing a cap. That is, if either hand is above the head, we should print "Someone is hailing a taxi!". 

All code edits should occur in assignment.py in the src folder.

There are two parts to this task:
1. install and run the assignment.py script (70%)
2. implement the code to be able to dectect someone hailing (30%)


## Part 1
### Dependencies

You need to install dependencies below.

- python3
- tensorflow 1.4.1+
- opencv3, protobuf, python3-tk

The point of this assignment for you to research what is required and how it can be installed.
### Install

```bash
$ git clone https://www.github.com/ishaanv/tf-openpose
$ cd tf-openpose
$ pip3 install -r requirements.txt
```

Requirements files in python contain some of the dependencies.

## Demo

### Test Inference (one the dependencies are installed)

You can test the inference feature with a by capturing video from your webcam.

```
$ python3 src/assignment.py
```

<!-- Or if that doesn't whatever reason, test the inference feature with a single image.

```
$ python3 src/assignment.py --image=...
``` -->

Then you will see the screen as below with pafmap, heatmap, result and etc.

![inferent_result](./etcs/inference_result2.png)

## Part 2

Read the code and TODOs in assignment.py. Uncomment the line:
```
print([(POSE_COCO_BODY_PARTS[k], v.x, v.y) for k,v in human.body_parts.items()])
```
and run it to see what happens.

## Deadline

1 May 2018. Marking will be done in the labs on the day.

## References

### OpenPose

[1] https://github.com/CMU-Perceptual-Computing-Lab/openpose

[2] Training Codes : https://github.com/ZheC/Realtime_Multi-Person_Pose_Estimation

[3] Custom Caffe by Openpose : https://github.com/CMU-Perceptual-Computing-Lab/caffe_train

[4] Keras Openpose : https://github.com/michalfaber/keras_Realtime_Multi-Person_Pose_Estimation

### Lifting from the deep

[1] Arxiv Paper : https://arxiv.org/abs/1701.00295

[2] https://github.com/DenisTome/Lifting-from-the-Deep-release

### Mobilenet

[1] Original Paper : https://arxiv.org/abs/1704.04861

[2] Pretrained model : https://github.com/tensorflow/models/blob/master/slim/nets/mobilenet_v1.md

### Libraries

[1] Tensorpack : https://github.com/ppwwyyxx/tensorpack

### Tensorflow Tips

[1] Freeze graph : https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/tools/freeze_graph.py

[2] Optimize graph : https://codelabs.developers.google.com/codelabs/tensorflow-for-poets-2
