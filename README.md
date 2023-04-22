# Robótica Lab 3
## Instalación de ROS y prueba de turtlesim
Lo primero que se hizo para el desarrollo de este laboratorio fue instalar todas las herramientas necesarias y comprobar la instalación usando turtlesim. Esto siguiendo la documentación de ROS y el tutorial sugerido en la guía de laboratorio.

![instalacion](https://i.imgur.com/By5I19l.png)

## Scripts de Matlab
(Estos scripts se pueden encontrar en la carpeta `matlab` de este repositorio.)

Se usa el script dado en la guía para inicializar la conexión.
```matlab
%%
rosinit; %Conexión con nodo maestro
%%
velPub = rospublisher('/turtle1/cmd_vel', 'geometry_msgs/Twist'); %Creación publicador
velMsg = rosmessage(velPub); %Creación de mensaje
%%
velMsg.Linear.X = 1; %Valor del mensaje
send(velPub,velMsg); %Envio
pause(1)
```
![script_1](https://i.imgur.com/hF9WgCB.png)

Luego, se es escribe el segundo script solicitado para obtener el `rossubscriber` y su campo `LatestMessage`
```matlab
sub = rossubscriber('/turtle1/pose', 'turtlesim/Pose');
latest = sub.LatestMessage;
```
![script_2](https://i.imgur.com/wCxWg5d.png)

Para responder a la pregunta planteada en la guía, el nodo maestro se puede finalizar usando la función `rosshutdown` de Matlab.
![shutdown](https://i.imgur.com/b3rFxFU.png)

## Python
El script que se escribió para cumplir con los resutlados enunciados en la guía de laboratorio se puede encontrar en la carpeta `python`.

El script se escribió basandonos en los scripts incluidos por defecto en turtlesim. Se analizaron algunas de las funciones usadas y se les realizaron las modificaciones apropiadas.

Tras esto, se ejecutaron los comandos listados en la guía del laboratorio.

Los resultados se pueden ver en las capturas de pantalla publicadas a lo largo de este informe y en el video que se encuentra en la carpeta `video` de este repositorio.