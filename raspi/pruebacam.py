#from picamera import PiCamera
#from picamera.array import PiRGBArray
#import picamera
import cv2
import os
from time import sleep

#camara = PiCamera()
#camara.resolution = (304,304)
#camara.framerate = 30
BASE_PATH = str(os.path.abspath(''))
PATH_CAPTURA = BASE_PATH
#raw = PiRGBArray(camara, size = (304,304))
cap = cv2.VideoCapture('rtsp://admin:admin@192.168.0.100/12')

#for image in camara.capture_continuous(raw, format = "bgr", use_video_port = True):
while True:
    #frame = image.array
    ret, frame = cap.read()
    cv2.imshow("ventana",frame)
    cv2.imwrite(PATH_CAPTURA + "/" + 'Captura4.jpg', frame)
    #raw.truncate(0)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break