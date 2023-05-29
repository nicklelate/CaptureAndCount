import cv2
from cv2 import *
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from numpy.lib.polynomial import poly
import datetime

b = True
run = 1
while b:
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)
    result, image = cam.read()
    x = datetime.datetime.now()
    y = x.strftime("%M")
    if int(y[1])%5 == 0:
        if run == 1:
            if result:
                cv2.imwrite("GeeksForGeeks.png", image)
                img = cv2.imread("GeeksForGeeks.png")
                box,label,count = cv.detect_common_objects(img)
                count = 0
                for i in label:
                    if i == 'person':
                        count += 1
                print("there are " + str(count) + " people.")
            else:
                print("No image detected. Please! try again")
            print(x)
            run = 0
    else:
        run = 1