#!/usr/bin/env python

import rospy                                                    # Se importa las librerias o modulos necesarios para que se pueda leer python en ross
from std_msgs.msg import String                                 # se establece que tipo de entrada se va a leer, en este caso es un string del tòpico std_msgs

def talker():                                                   # Se define quien va a publicar el mensaje al tòpico (chatter), en este caso serà el talker
    pub = rospy.Publisher('chatter', String, queue_size=10)     # Publisher es el comando que publica la acciòn, en el cual se tienen que especificar las siguientes caracterìsticas del tòpico: el nombre, tipo de mensaje y las veces que se va a enviar 
                                                                
                                                                # Cada nodo debe de tener su propio nombre, por lo que no pueden tener el mismo nombre
    
    rospy.init_node('talker', anonymous=True)                   # anonymous=True flag es el encargado de escoger el ùnico nodo. Nombre del nodo 'talker' 
    rate = rospy.Rate(1)                                        # 1Hz, sirve para controlar la velocidad de la chatter, se cambia para que se pueda visualizar mejor su movimiento 
    
    i = 0
    while not rospy.is_shutdown():                              # El ciclo while va a estarse ejecuntando hasta que se llame el comando CTRL+C
        
        hello_str = "hello world %s" % i                        # Se crea el mensjae que se desea mostrar, este mesnsaje debe de ser un string ya que se especifica arriba que tipo de mensaje se va a aleere, de igual manera se agrega lo del contador
        rospy.loginfo(hello_str)                                # Se carga el mensaje en terminator 
        pub.publish(hello_str)                                  # Se publica el mensjae en el tòpico que es la chatter  publish the message to the topic
        rate.sleep()                                            # El comando sleep es el que se encarga de esperar el tiempo especifico para iniciar otro ciclo
        i=i+1                                                   # Se va aumentando 1 al contador cada termina un ciclo


if name == 'main':
    try:
        talker()                                                # Se llama la funciòn talker
    except rospy.ROSInterruptException:
        pass