#!/usr/bin/env python
# license removed for brevity

import rospy                                                                # Importa la libreria de ROS en Python
from geometry_msgs.msg import Twist                                         # Importa el tipo de mensaje Twist de geometry_msgs

def talker():

    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)         # Genera un nuevo Publisher encargado de el topico turtle 1, con el tipo de mensaje Twist y un queue size definido el cual regula cuantos mensajes puede mandar.

    rospy.init_node('talker', anonymous=True)                               # Inicializa el nodo talker, al usar la flag anonymous=True rospy generara un nombre unico para el nodo talker.

    rate = rospy.Rate(1)                                                    # Define el tasa de refresco del ciclo a 1 Hz, esto afecta la velocidad 

    while not rospy.is_shutdown():                                          # While que seguira publicando hasta que Ctrl+C sea presionado

        twist_msg = Twist()
        twist_msg.linear.x = 0.5                                            # Genera un nuevo mensaje Twist y determina la velocidad linear en X a 0.5
        pub.publish(twist_msg)                                              # Genera la publicacion con el mensaje definido
        twist_msg.linear.y = 0.5                                            # Genera un nuevo mensaje Twist y determina la velocidad linear en Y a 0.5
        pub.publish(twist_msg) 
        rate.sleep()                                                        # Procede a esperar hasta que termine el ciclo

if __name__ == '__main__':                                                  # Corre la funcion Talker si es definida como el archivo a correr (main)

    try:
        talker()
    except rospy.ROSInterruptException:
        pass                                                                # Si hay una Exception de ROS procede a llamar un pass

