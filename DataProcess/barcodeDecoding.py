import pyzbar as pzb
import cv2 
from matplotlib import pyplot as plt

# TODO: This code is useless due to the poor quality of the capture device.

captureDevice = cv2.VideoCapture(0) #? "0" is the device index.




def take_photo(photoName:str):

    frame = captureDevice.read()[1]
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    cv2.imwrite(photoName+".jpeg",frame_rgb)


take_photo("test")


captureDevice.release() #? It turns off the capture device.
