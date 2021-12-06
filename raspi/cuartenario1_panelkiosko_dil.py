#################### Marco De Importaciones ######################
import tensorflow as tf
import numpy as np
import os
#import random
#import picamera
#from picamera import PiCamera
#from picamera.array import PiRGBArray
import time
import cv2
from skimage.io import imread
from skimage.transform import resize
#from skimage.transform import resize
#from skimage.color import rgb2gray
import requests

print('Importaciones Realizadas')

################### Constantes del programa ######################

TOKEN = "BBFF-0iN09hVXKqGkZBdwTicwKbdfNOzPBI"

DEVICE_LABEL = "prueba"
VARIABLE_LABEL1 = "temperatura"

# Dimensiones de las imagenes RGB
IMG_WIDTH = 200
IMG_HEIGHT = 200
IMG_CHANNELS = 3

# path base
BASE_PATH = str(os.path.abspath(''))

if ('\\' in BASE_PATH) == True:
    separator_dir = '\\'
else:
   separator_dir = '/'
   
# path modelos

U_NET_PATH = BASE_PATH + separator_dir + 'Modelos_h5' + separator_dir + 'Modelo_U_Net.h5'

CLASIFICADOR_CUATERNARIO = BASE_PATH + separator_dir + 'Modelos_h5' + separator_dir + 'Clasificacion_cuaternaria.h5'

# path Captura

PATH_CAPTURA = BASE_PATH + separator_dir + 'Captura'

# Objeto camara

#camara = picamera.PiCamera()
#camara.resolution = (IMG_WIDTH,IMG_HEIGHT)
#camara.framerate = 30

#raw = PiRGBArray(camara, size = (IMG_WIDTH,IMG_HEIGHT))

# imagen

imagen = np.zeros((1, IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype = np.uint8)

# modelo U-net

U_NET = tf.keras.models.load_model(U_NET_PATH)

# Modelo Clasificacion

CLASIFICADOR = tf.keras.models.load_model(CLASIFICADOR_CUATERNARIO)

# opent .txt file

print('Constantes Establecidas')

################### Ciclo de inferencias ######################
print('Inicio de proceso')
#print(clicks_x)
#for image in camara.capture_continuous(raw, format = "bgr", use_video_port = True):
cap = cv2.VideoCapture('rtsp://admin:admin@192.168.0.100/12')
contador = 1
kernel = np.ones((6,6), np.uint8)

while True:
    # Actualizacion de la iteracion 
    print('----------------------------------------')
    
    #frame = image.array
    
    #img = cv2.resize(frame, (IMG_HEIGHT, IMG_WIDTH), interpolation = cv2.INTER_AREA)
    
    #cv2.imshow("original",frame)
    
    #camara.capture(PATH_CAPTURA + separator_dir + 'Captura.jpg',resize=(200,200))
    ret, frame = cap.read()
    cv2.imwrite(PATH_CAPTURA + separator_dir + 'Captura.jpg', frame)
    
    #ret, frame = cap.read()
    
    #cv2.imwrite(PATH_CAPTURA + separator_dir + 'Captura.png', frame)
    
    #cv2.imshow("original",frame)
    
    img = imread(PATH_CAPTURA + separator_dir + 'Captura.jpg')[:,:,:IMG_CHANNELS]
    
    cv2.imshow("original",img)
    
    img = resize(img, (IMG_HEIGHT, IMG_WIDTH), mode = 'constant', preserve_range = True)

    imagen[0] = img
    
    
    
    #mascara
    mask_predict = U_NET.predict(imagen, verbose = 0)
    mask_predict = (mask_predict > 0.7).astype(np.uint8)
    #print(mask_predict.shape)
    
    #mask_predict2 = imread(PATH_CAPTURA + separator_dir + 'mask.jpg')[:,:,:IMG_CHANNELS]
    
    img_dilation = cv2.dilate(mask_predict[0,:,:,0], kernel, iterations = 1)
    
    
    #print("img.shape: ", img.shape)
    #print("mask_predict.shape: ", mask_predict.shape)
    
    mask_predict[0,:,:,0] = img_dilation
    
    mask_image = mask_predict*imagen

    prueba = mask_image[0,:,:,:]
    cv2.imshow("mask",prueba)
    
    # Clasificacion

    Class_predict = CLASIFICADOR.predict(mask_image, verbose = 0)
    Class_predict = (Class_predict>0.5).astype(np.uint8)
    index = list(Class_predict[0]).index(1)

    if index == 0:
        Clase = 'Fisura'
        value_1 = 1
    elif index == 1:
        Clase = 'Sombra'
        value_1 = 1
    elif index == 2:
        Clase = 'Polvo'
        value_1 = 1
    elif index == 3:
        Clase = 'Sin Falla'
        value_1 = 0

    print('Clasificacion: ',Clase)
    contador = contador + 1
    
    #payload = {VARIABLE_LABEL1: {"value":value_1,"context":{"index":index}}}
    #print("[INFO] Attemping to send data")
    
    #url = "http://industrial.api.ubidots.com"
    #url = "{}/api/v1.6/devices/{}".format(url,DEVICE_LABEL)
    #headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    #status = 400
    #attempts = 0
    #while status >= 400 and attempts <= 5:
    #    req = requests.post(url=url, headers = headers, json=payload)
    #    status = req.status_code
    #    attempts += 1
    #    time.sleep(1)

    #print(req.status_code, req.json())
    #if status >= 400:
    #    print("[ERROR] Could not send data after 5 attempts, please check your token credentials and internet connection")
    #else:
    #    print("[INFO] request made properly, your device is updated")
    
    #print("[INFO] finished")
    
    
    #.truncate(0)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break


