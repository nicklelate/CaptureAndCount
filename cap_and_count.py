import cv2
from cv2 import *
import cvlib as cv
import datetime
import time
from firebase import firebase
# python -m pip install

url = 'https://cmudigitaltwin-default-rtdb.asia-southeast1.firebasedatabase.app/'
messenger = firebase.FirebaseApplication(url)
b = True
run = 1
while b:
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)
    result, image = cam.read()
    x = datetime.datetime.now()
    if result:
        cv2.imwrite("818_room.png", image)
        img = cv2.imread("818_room.png")
        box,label,count = cv.detect_common_objects(img)
        count = 0
        for i in label:
            if i == 'person':
                count += 1
        print("there are " + str(count) + " people.")
    else:
        print("No image detected. Please! try again")

    engineer = {'Timestamp':x,'People':count}

    result = messenger.put('/818 room','CCTV',engineer)

    print("Engineer 1", result)
    time.sleep(300)
