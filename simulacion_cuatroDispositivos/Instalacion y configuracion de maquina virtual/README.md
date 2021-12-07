# Instalacion y configuracion de maquina virtual

## Descarga de VMware Workstation Player

La herramienta utilizada para la creación de las distintas máquinas virtuales es *VMware Workstation Player*. Esta herramienta puede ser descargada desde su [página oficial](https://www.vmware.com/co/products/workstation-player/workstation-player-evaluation.html).
![Página VMware Workstation Player](https://github.com/jahernandezr1/proyecto_ielc/blob/master/simulacion_cuatroDispositivos/Instalacion%20y%20configuracion%20de%20maquina%20virtual/Figuras%20README/vmware.PNG)
**NOTA:** Para poder crear las máquinas virtuales, su dispositivo debe tener habilitada la virtualización desde BIOS.
Luego de instalar *VMware Workstation Player* debe seleccionar el uso de licencia no comercial para poder utilizar el programa.


## Descarga de la imagen ISO
La imagen ISO que se usará para la máquina virtual Raspbian se puede descargar [aquí](https://www.raspberrypi.com/software/raspberry-pi-desktop/)
y se llama Raspberry Pi Desktop.
![Imagen ISO](https://github.com/jahernandezr1/proyecto_ielc/blob/master/simulacion_cuatroDispositivos/Instalacion%20y%20configuracion%20de%20maquina%20virtual/Figuras%20README/tutorial0.PNG)


## Creación de las Máquinas Virtuales
El primer paso es seleccionar la opción *Create a New Virtual Machine*

![Paso 1](https://github.com/jahernandezr1/proyecto_ielc/blob/master/simulacion_cuatroDispositivos/Instalacion%20y%20configuracion%20de%20maquina%20virtual/Figuras%20README/tutorial1.png)

Ahora, debe seleccionar la opción *Installer disc image file (iso)* y luego debe buscar la imagen ISO que descargó anteriormente.

![Paso 2](https://github.com/jahernandezr1/proyecto_ielc/blob/master/simulacion_cuatroDispositivos/Instalacion%20y%20configuracion%20de%20maquina%20virtual/Figuras%20README/tutorial2.png)

Lo siguiente será seleccionar *Linux* como sistema operativo y la versión *Debian 9.x 64-bit*

![Paso 3](https://github.com/jahernandezr1/proyecto_ielc/blob/master/simulacion_cuatroDispositivos/Instalacion%20y%20configuracion%20de%20maquina%20virtual/Figuras%20README/tutorial3.png)

En momento debe asignar un nombre y una carpeta donde se guardarán todos los archivos de la máquina virtual. Es muy recomendable que si crea varias máquinas virtuales les asigne una carpeta diferente a cada una.

![Paso 4](https://github.com/jahernandezr1/proyecto_ielc/blob/master/simulacion_cuatroDispositivos/Instalacion%20y%20configuracion%20de%20maquina%20virtual/Figuras%20README/tutorial4.png)

Posteriormente deberá definir un espacio en memoria para los archivos de la máquina virtual. Para este proyecto se utilizará el tamaño recomendado. Luego, se recomienda dividir el disco virtual en múltiples archivos por si se desea mover la máquina virtual en algún momento.

![Paso 5](https://github.com/jahernandezr1/proyecto_ielc/blob/master/simulacion_cuatroDispositivos/Instalacion%20y%20configuracion%20de%20maquina%20virtual/Figuras%20README/tutorial5.png)

En este punto le deberá aparecer un resumen de las opciones seleccionadas anteriormente, así como los recursos con los que se configurará inicialmente la máquina virtual. Cabe aclarar que estos recursos pueden ser modificados presionando el botón *Customize Hardware*, sin embargo, para este proyecto se dejarán los valores que están por defecto. Es importante mencionar que estos recursos se pueden modificar en cualquier momento futuro.

![Paso 6](https://github.com/jahernandezr1/proyecto_ielc/blob/master/simulacion_cuatroDispositivos/Instalacion%20y%20configuracion%20de%20maquina%20virtual/Figuras%20README/tutorial6.png)

Aquí se termina la configuración de la máquina virtual. Lo siguiente será seleccionar la máquina virtual que se acabó de crear y luego debe dar clic en *Play virtual machine*.

![Paso 7](https://github.com/jahernandezr1/proyecto_ielc/blob/master/simulacion_cuatroDispositivos/Instalacion%20y%20configuracion%20de%20maquina%20virtual/Figuras%20README/tutorial7.png)

Desde aquí iniciará la instalación de Raspbian. Debe seleccionar la opción *Graphical install* seguido de la tecla **enter**.
![Paso 8](https://github.com/jahernandezr1/proyecto_ielc/blob/master/simulacion_cuatroDispositivos/Instalacion%20y%20configuracion%20de%20maquina%20virtual/Figuras%20README/tutorial8.png)

Ahora, debe seleccionar la configuración del teclado que desea utilizar.

![Paso 9](https://github.com/jahernandezr1/proyecto_ielc/blob/master/simulacion_cuatroDispositivos/Instalacion%20y%20configuracion%20de%20maquina%20virtual/Figuras%20README/tutorial9.png)

Lo siguiente será seleccionar *Guided - use entire disk*.
![Paso 10](https://github.com/jahernandezr1/proyecto_ielc/blob/master/simulacion_cuatroDispositivos/Instalacion%20y%20configuracion%20de%20maquina%20virtual/Figuras%20README/tutorial10.png)

En esta ocasión debe seleccionar el disco que utilizará, sin embargo, solamente debería aparecer uno.
![Paso 11](https://github.com/jahernandezr1/proyecto_ielc/blob/master/simulacion_cuatroDispositivos/Instalacion%20y%20configuracion%20de%20maquina%20virtual/Figuras%20README/tutorial11.png)

A continuación debe seleccionar *All files in one partition (recommended for new users)*.
![Paso 12](https://github.com/jahernandezr1/proyecto_ielc/blob/master/simulacion_cuatroDispositivos/Instalacion%20y%20configuracion%20de%20maquina%20virtual/Figuras%20README/tutorial12.png)

Le debe aparecer un resumen con la confirmación de las operaciones realizadas. Puede oprimir *Continue*.
![Paso 13](https://github.com/jahernandezr1/proyecto_ielc/blob/master/simulacion_cuatroDispositivos/Instalacion%20y%20configuracion%20de%20maquina%20virtual/Figuras%20README/tutorial13.png)

En este momento le aparecerá una ventana de confirmación, debe marcar la opción *Yes*.
![Paso 14](https://github.com/jahernandezr1/proyecto_ielc/blob/master/simulacion_cuatroDispositivos/Instalacion%20y%20configuracion%20de%20maquina%20virtual/Figuras%20README/tutorial14.png)

Lo siguiente será seleccionar la opción *Yes*.
![Paso 15](https://github.com/jahernandezr1/proyecto_ielc/blob/master/simulacion_cuatroDispositivos/Instalacion%20y%20configuracion%20de%20maquina%20virtual/Figuras%20README/tutorial15.png)

Lo siguiente será seleccionar */dev/sda*.
![Paso 16](https://github.com/jahernandezr1/proyecto_ielc/blob/master/simulacion_cuatroDispositivos/Instalacion%20y%20configuracion%20de%20maquina%20virtual/Figuras%20README/tutorial16.png)

Aquí debería aparecer un mensaje de instalación completada.
![Paso 17](https://github.com/jahernandezr1/proyecto_ielc/blob/master/simulacion_cuatroDispositivos/Instalacion%20y%20configuracion%20de%20maquina%20virtual/Figuras%20README/tutorial17.png)

Se finalizó con éxito la instalación de Raspbian, ahora, sigue una pequeña configuración de la Raspberry.
![Paso 18](https://github.com/jahernandezr1/proyecto_ielc/blob/master/simulacion_cuatroDispositivos/Instalacion%20y%20configuracion%20de%20maquina%20virtual/Figuras%20README/tutorial18.png)

El siguiente paso será configurar el país, lenguaje y zona horario que utilizará.
![Paso 19](https://github.com/jahernandezr1/proyecto_ielc/blob/master/simulacion_cuatroDispositivos/Instalacion%20y%20configuracion%20de%20maquina%20virtual/Figuras%20README/tutorial19.png)

Por último, deberá ingresar una contraseña que le servirá para iniciar sesión en el dispositivo.
![Paso 20](https://github.com/jahernandezr1/proyecto_ielc/blob/master/simulacion_cuatroDispositivos/Instalacion%20y%20configuracion%20de%20maquina%20virtual/Figuras%20README/tutorial20.png)


## Instalación de Software Necesario
Para poder realizar esta simulación es necesario que todas las máquinas virtuales que vayan a participar tengan instalados el paquete *paho-mqtt* con el fin de que podamos enviar mensajes de tipo *MQTT* en python y, también, es necesario instalar mosquitto, que será lo que permitirá la comunicación entre los distintos dispositivos.

Lo primero que debe hacer es abrir la terminal de la máquina virtual y correr los siguientes comandos:

>>> sudo apt update -y
>>> sudo apt install mosquitto mosquitto-clients -y
>>> sudo pip install paho-mqtt

Con esto ya debería ser capaz de correr los códigos necesarios para la simulación.
