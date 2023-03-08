#!/usr/bin/env python
import rospy                                                                # Importa la libreria de Python en ROS
from std_msgs.msg import String                                             # Importa el tipo de mensaje String de std_msgs

def chatter_callback(message):                                              # Esta funcion es llamada cada que se reciba un mensaje
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", message.data)       # Imprime el mensaje recibido junto al nombre del nodo

def listener():                                                             # Define la funcion listener

    rospy.init_node('listener', anonymous=True)                             # Inicializa el nodo listener, al usar la flag anonymous=True rospy generara un nombre unico para el nodo talker

    rospy.Subscriber("chatter", String, chatter_callback)                   # Genera el subscriber chatter y define la funcion del callback

    rospy.spin()                                                            # spin() se encarga de mantener la ejecucion de python exisitendo hasta que el nodo deje de correr

if __name__ == '__main__':                                                  # Corre la funcion listener si es definida como el archivo a correr (main)

    listener()                                                              # Instancia la funcion listener para llamarla



