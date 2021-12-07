# Simulación - Cuatro Dispositivos

Por temas de tiempo y recursos no fue posible realizar una prueba de campo con cinco dispositivos Raspberry Pi y cuatro paneles solares. Sin embargo, se realizó una simulación con cuatro máquinas virtuales y una Raspberry Pi real. Donde tres máquinas virtuales y la Raspberry Pi simularon ser dispositivos que detectan fallas en paneles solares en tiempo real y la máquina virtual restante simuló ser un gateway. Las cuatro máquinas virtuales fueron creadas con una imagen de Raspbian y con el sistema operativo Debian 9.x 64-bit.

## Objetivo
El principal objetivo de esta prueba fue simular la conexión entre cinco dispositivos, poder enviar y recibir mensajes entre ellos y enviar información resultante a Ubidots.
