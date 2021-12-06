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

print('Importaciones Realizadas')

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

CLASIFICADOR_CUATERNARIO = BASE_PATH + separator_dir + 'Modelos_h5' + separator_dir + 'Clasificacion_cuaternaria.h5'

# path Captura

PATH_CAPTURA = BASE_PATH + separator_dir + 'imgs'

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
#for image in camara.capture_continuous(raw, format = "bgr", use_video_port = True):
while True:
    # Actualizacion de la iteracion
    print('----------------------------------------')
    #frame = image.array
    #img = cv2.resize(frame, (IMG_HEIGHT, IMG_WIDTH), interpolation = cv2.INTER_AREA)
    
    #cv2.imshow("original",frame)
    
    #camara.capture(PATH_CAPTURA + separator_dir + 'Captura.png',resize=(200,200))
    
    img = cv2.imread(PATH_CAPTURA + separator_dir + 'tierra3.jpg')
    
    cv2.imshow("original",img)
    
    img = cv2.resize(img, (IMG_HEIGHT, IMG_WIDTH), interpolation = cv2.INTER_AREA)

    imagen[0] = img
    
    #mascara
    
    mask_predict = U_NET.predict(imagen, verbose = 0)
    mask_predict = (mask_predict > 0.7).astype(np.uint8)

    print("img.shape")
    print(img.shape)

    print("mask_predict.shape")
    print(mask_predict.shape)
    
    mask_image = mask_predict*img
    print("mask_image.shape")
    print(mask_image.shape)
    
    #cv2.imshow("mask",mask_image)
    img_mask = mask_image[0,:,:,:]
    cv2.imshow("mask",img_mask)
    
    # Clasificacion

    Class_predict = CLASIFICADOR.predict(mask_image, verbose = 0)
    #Class_predict = CLASIFICADOR.predict(imagen, verbose = 0)
    print(Class_predict)
    Class_predict = (Class_predict>0.5).astype(np.uint8)
    print(Class_predict)
    index = list(Class_predict[0]).index(1)

    if index == 0:
        Clase = 'Fisura'
    elif index == 1:
        Clase = 'Sombra'
    elif index == 2:
        Clase = 'Polvo'
    elif index == 3:
        Clase = 'Sin Falla'

    print('Clasificacion: ',Clase)
    
    
    #raw.truncate(0)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
