#################### Marco De Importaciones ######################
import tensorflow as tf
import numpy as np
import os
import random
import picamera
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import cv2
import requests

print('Importaciones Realizadas')


################### Constantes de Ubidots ######################
TOKEN = "BBFF-0iN09hVXKqGkZBdwTicwKbdfNOzPBI"

DEVICE_LABEL = "prueba"
VARIABLE_LABEL1 = "temperatura"

def build_payload(var1, index):
    if index == 0:
        value_1 = 0
    elif index == 1:
        value_1 = 1
    elif index == 2:
        value_1 = 2
    elif index == 3:
        value_1 = 3
    
    payload = {var1: value_1}

    return payload

def post_request(payload):
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url,DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers = headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    print(req.status_code, req.json())
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check your token credentials and internet connection")
        return False
    print("[INFO] request made properly, your device is updated")
    return True


################### Constantes del programa ######################

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

CLASIFICADOR_CUATERNARIO = BASE_PATH + separator_dir + 'Modelos_h5' + separator_dir + 'Clasificacion_binaria.h5'

# path Captura

PATH_CAPTURA = BASE_PATH + separator_dir + 'imgs'

# Objeto camara

#camara = picamera.PiCamera()
#camara.resolution = (IMG_WIDTH,IMG_HEIGHT)
#camara.framerate = 30

#raw = PiRGBArray(camara, size = (IMG_WIDTH,IMG_HEIGHT))

# imagen

imagen = np.zeros((1, IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype = np.uint8)
mask2 = np.zeros((1, IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype = np.uint8)

# modelo U-net

U_NET = tf.keras.models.load_model(U_NET_PATH)

# Modelo Clasificacion

CLASIFICADOR = tf.keras.models.load_model(CLASIFICADOR_CUATERNARIO)

# opent .txt file

print('Constantes Establecidas')

################### Ciclo de inferencias ######################
print('Inicio de proceso')
#for image in camara.capture_continuous(raw, format = "bgr", use_video_port = True):
while True:
    # Actualizacion de la iteracion
    print('----------------------------------------')
    #frame = image.array
    #img = cv2.resize(frame, (IMG_HEIGHT, IMG_WIDTH), interpolation = cv2.INTER_AREA)
    
    #cv2.imshow("original",frame)
    
    #camara.capture(PATH_CAPTURA + separator_dir + 'Captura.png',resize=(200,200))
    
    img = cv2.imread(PATH_CAPTURA + separator_dir + 'sombra3.jpg')
    mask = cv2.imread(PATH_CAPTURA + separator_dir + 'sombra3.png')
    
    #cv2.imshow("original",img)
    
    img = cv2.resize(img, (IMG_HEIGHT, IMG_WIDTH), interpolation = cv2.INTER_AREA)
    mask = cv2.resize(mask, (IMG_HEIGHT, IMG_WIDTH), interpolation = cv2.INTER_AREA)

    mask2[0] = mask
    
    #mascara
    
    #mask_predict = U_NET.predict(imagen, verbose = 0)
    #mask_predict = (mask_predict > 0.7).astype(np.uint8)
    
    
    mask_image = mask2*img
    
    #img_mask = mask_image[0,:,:,:]
    #cv2.imshow("mask",img_mask)
    
    # Clasificacion

    Class_predict = CLASIFICADOR.predict(mask_image, verbose = 0)
    #Class_predict = CLASIFICADOR.predict(imagen, verbose = 0)
    print(Class_predict)
    Class_predict = (Class_predict>0.5).astype(np.uint8)
    print(Class_predict)
    index = list(Class_predict[0]).index(1)

    if index == 0:
        Clase = 'Falla'
    elif index == 1:
        Clase = 'No falla'
    #elif index == 2:
    #    Clase = 'Polvo'
    #elif index == 3:
    #    Clase = 'Sin Falla'
        
    print('Clasificacion: ',Clase)
    
    payload = build_payload(VARIABLE_LABEL1, index)
    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] finished")
    
    #raw.truncate(0)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
