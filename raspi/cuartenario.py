#################### Marco De Importaciones ######################
import tensorflow as tf
#import tflite_runtime as tf

import numpy as np
#import matplotlib.pyplot as plt
import os
import random
import picamera
import time
#from skimage.io import imread
#from skimage.transform import resize
import cv2

print('Importaciones Realizadas')

################### Constantes del programa ######################

# Semilla de numeros aleatorios
#seed = 2020
#np.random.seed(seed)

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

####print("U_NET_PATH")
####print(U_NET_PATH)
CLASIFICADOR_CUATERNARIO = BASE_PATH + separator_dir + 'Modelos_h5' + separator_dir + 'Clasificacion_cuaternaria.h5'

####print("CLASIFICADOR_CUATERNARIO")
####print(CLASIFICADOR_CUATERNARIO)

# path Captura

PATH_CAPTURA = BASE_PATH + separator_dir + 'Captura'
####print("PATH_CAPTURA")
####print(PATH_CAPTURA)
# Tiempo de inicio

Tiempo_inicio = time.time()

# Objeto camara

camera = picamera.PiCamera()

# iteracion

iteracion = 0

# imagen

imagen = np.zeros((1, IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype = np.uint8)


# modelo U-net

U_NET = tf.keras.models.load_model(U_NET_PATH)

# Modelo Clasificacion

CLASIFICADOR = tf.keras.models.load_model(CLASIFICADOR_CUATERNARIO)

# opent .txt file

file = open(BASE_PATH + separator_dir + 'Data'+ separator_dir +str(np.random.randint(1,100)) + '.txt','w')
file.write('Iteracion,Tiempo_Captura,Tiempo_Preprocesado,Tiempo_Segmentacion,Clase,Tiempo_Clasificacion\n')
print('Constantes Establecidas')

################### Ciclo de inferencias ######################
print('Inicio del ciclo de inferencias')

while True:

    # Actualizacion de la iteracion
    print('----------------------------------------')
    
    iteracion += 1
    if iteracion == 100: break
    print('Iteracion: ', iteracion)
    file.write(str(iteracion)+',')
    
    # Captura de la imagen

    Tiempo_Nueva_iteracion = time.time()

    camera.capture(PATH_CAPTURA + separator_dir + 'Captura.png',resize=(200,200))

    Tiempo_captura = [time.time(), time.time() - Tiempo_Nueva_iteracion]

    print('Tiempo de captura: ', Tiempo_captura[1])
    file.write(str(Tiempo_captura[1])+',')

    # Procesamiento de la imaen

    #img = imread(PATH_CAPTURA + separator_dir + 'Captura.jpg')[:,:,:IMG_CHANNELS]
    img = cv2.imread(PATH_CAPTURA + separator_dir + 'Captura.png')
    
    #img = resize(img, (IMG_HEIGHT, IMG_WIDTH), mode = 'constant', preserve_range = True)
    img = cv2.resize(img, (IMG_HEIGHT, IMG_WIDTH), interpolation = cv2.INTER_AREA)

    imagen[0] = img

    Tiempo_preprocesado_captura = [time.time(), time.time() - Tiempo_captura[0]]

    print('Tiempo de pre-procesado captura: ', Tiempo_preprocesado_captura[1])
    file.write(str(Tiempo_preprocesado_captura[1])+',')
    
    # Segmentacion Semantica U-Net

    mask_predict = U_NET.predict(imagen, verbose = 0)
    mask_predict = (mask_predict > 0.7).astype(np.uint8)
    
    mask_image = mask_predict*imagen
   
    #plt.imshow(mask_image[0])
    #plt.show()

    Tiempo_segmentacion_semantica = [time.time(), time.time() - Tiempo_preprocesado_captura[0]]

    print('Tiempo de Segmentacion Semantica: ', Tiempo_segmentacion_semantica[1])
    file.write(str(Tiempo_segmentacion_semantica[1])+',')
    
    # Clasificacion

    Class_predict = CLASIFICADOR.predict(mask_image, verbose = 0)
    Class_predict = (Class_predict>0.5).astype(np.uint8)
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
    file.write(Clase +',')

    Tiempo_clasificacion = [time.time(), time.time() - Tiempo_segmentacion_semantica[0]]

    print('Tiempo de Clasificacion: ', Tiempo_clasificacion[1])
    file.write(str(Tiempo_clasificacion[1])+'\n')

file.close()
