import argparse
import logging
import time

import cv2
import numpy as np

#import pyautogui
import common
from estimator import TfPoseEstimator
from networks import get_graph_path, model_wh

import platform
import os
#Imports extensions, adds neccessary functions for the code. Note: these are written by others

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#Os module- extension for read/write files, manipulate paths etc.
#Environ- Sets up the preferred os environment

logger = logging.getLogger('TfPoseEstimator-WebCam')
#Logs into webcam?

logger.setLevel(logging.CRITICAL)
#sets the threshold for logging to critical (numerical value of 50)

ch = logging.StreamHandler()
#Sends the outputs to any object/filetype? which supports write() and flush() methods/functions?. 
#There are also two other handler besides StreamHandler, these are NullHandler and FileHandler

ch.setLevel(logging.CRITICAL)
#sets the threshold for ch variable or our Streamhandler to critical

formatter = logging.Formatter(
    '[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

fps_time = 0

#
POSE_COCO_BODY_PARTS = {
    0: "Nose",
    1: "Neck",
    2: "RShoulder",
    3: "RElbow",
    4: "RWrist",
    5: "LShoulder",
    6: "LElbow",
    7: "LWrist",
    8: "RHip",
    9: "RKnee",
    10: "RAnkle",
    11: "LHip",
    12: "LKnee",
    13: "LAnkle",
    14: "REye",
    15: "LEye",
    16: "REar",
    17: "LEar",
    18: "Background",
}

# call this when a taxi is being hailed!
def hail_taxi(img):
    print("Someone is hailing a taxi!")
    cv2.putText(img, "TAXI!",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (94, 218, 255), 2)
    cv2.putText(img, platform.uname().node,
                    (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

if __name__ == '__main__':
    # arguements to your program
    parser = argparse.ArgumentParser(
        description='tf-pose-estimation realtime webcam')
    parser.add_argument('--camera', type=int, default=0)
    parser.add_argument('--zoom', type=float, default=1.0)
    parser.add_argument(
        '--resolution',
        type=str,
        default='432x368',
        help='network input resolution. default=432x368')
    parser.add_argument(
        '--model',
        type=str,
        default='mobilenet_thin',
        help='cmu / mobilenet_thin')
    parser.add_argument(
        '--show-process',
        type=bool,
        default=False,
        help='for debug purpose, if enabled, speed for inference is dropped.')
    args = parser.parse_args()

    w, h = model_wh(args.resolution)
    e = TfPoseEstimator(get_graph_path(args.model), target_size=(w, h))
    camera = cv2.VideoCapture(args.camera)
    ret_val, image = camera.read()
    
    print("**** CTRL+C to exit ****")
    while True:
        # get image form the camera
        ret_val, image = camera.read()
        # boilerplate
        canvas = np.zeros_like(image)
        img_scaled = cv2.resize(
            image,
            None,
            fx=args.zoom,
            fy=args.zoom,
            interpolation=cv2.INTER_LINEAR)
        dx = (canvas.shape[1] - img_scaled.shape[1]) // 2
        dy = (canvas.shape[0] - img_scaled.shape[0]) // 2
        canvas[dy:dy + img_scaled.shape[0], dx:
               dx + img_scaled.shape[1]] = img_scaled
        image = canvas
        # feed image into the neural network
        humans = e.inference(image)  # list of humans
        for id, human in enumerate(humans):

            # TODO ensure it only does this when someone is hailing a taxi.
            # That is, an arm is above their head.

            HumanPose = [(POSE_COCO_BODY_PARTS[k], v.x, v.y) for k,v in human.body_parts.items()]
            
            try: 
                REyeCoord = [yCoordin for (BodyParts, xCoordin, yCoordin) in HumanPose if BodyParts == 'REye']
            except:
                pass
            
            try:
                RWristCoord = [yCoordin for (BodyParts, xCoordin, yCoordin) in HumanPose if BodyParts == 'RWrist']
                if RWristCoord[0] > REyeCoord[0]:
                    hail_taxi(image)
            except:
                pass
            
            try:
                LWristCoord = [yCoordin for (BodyParts, xCoordin, yCoordin) in HumanPose if BodyParts == 'LWrist']
                if LWristCoord[0] > REyeCoord[0]:
                    hail_taxi(image)
            except:
                pass


        # drawing lines on an image
        image = TfPoseEstimator.draw_humans(image, humans, imgcopy=False)

        # FPS counter
        cv2.putText(image, "FPS: {:.2f}".format(1.0 / (time.time() - fps_time)),
                    (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (128, 0, 0), 2)
        cv2.imshow('tf-pose-estimation result', image)
        fps_time = time.time()
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()

#Test Push to repo: brightonjake
# test commit: elijah, Kevin

#Co-author test