# El proceso para proponer los pasos de solución para el control de posición en un eje o en su defecto implementarlo.

1.  Primero, iniciamos el turtlesim. En una terminal, se escribe “roscore” para iniciar el ROS core y luego se escribe “rosrun turtlesim turtlesim_node” para iniciar el simulador de turtlesim.
2.  Seguidamente, se escribe un nodo ROS para controlar la posición de la tortuga. Primero creamos un nuevo nodo ROS en una ventana de terminal separada usando el comando **“rosrun <nombre_paquete> <nombre_nodo>”.**. El nodo debe suscribirse al tema de pose de la tortuga **“(/turtle1/pose)”** y publicar en el tema de velocidad de la tortuga **“(/turtle1/cmd_vel)”**.
3.  A continuación, definimos la posición deseada donde determinamos la posición deseada para la tortuga en el eje o sistema complementario, dependiendo del planteamiento del problema.
4.  También, se calcula la posición actual de la tortuga donde se extrae la posición actual de la tortuga usando el comando “pose”.
5.  Igualmente, se calcula el error. El cálculo se da mediante la relación entre el error entre la posición actual y la posición deseada.
6.  Ahora, calculamos la entrada de control. Según el error, se calcula la entrada de control que acerque la tortuga a la posición deseada.
7.  Por consiguiente, definimos la entrada de control, donde la entrada de control en el tema de velocidad de la tortuga **“(/turtle1/cmd_vel)”**.
8.  Es así que se repita los pasos 4-7 hasta que la tortuga alcance la posición deseada hasta seguir repitiendo los pasos 4-7 hasta que la tortuga alcance la posición deseada.
9.  Por otra parte, para detener la tortuga una vez que la tortuga alcance la posición deseada, se detiene su movimiento publicando comandos de velocidad cero en el tema de velocidad de la tortuga **“(/turtle1/cmd_vel)”**.
10.  Por último, se verifica la posición de la tortuga. Verificamos que la tortuga haya alcanzado la posición deseada comprobando su posición usando el mensaje Pose del comando pose **“(/turtle1/pose)”**.

Siguiendo estos pasos, puedes resolver el control de posición en un eje o complementario usando turtlesim.
