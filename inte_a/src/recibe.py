#!/usr/bin/env python
import rospy
import random
from std_msgs.msg import Int16 
def llamado(numero):
     rospy.loginfo(rospy.get_caller_id() + "\t recibido %d \t " ,numero.data)
def recibe():
    rospy.init_node('llamado', anonymous=True) 
    rospy.Subscriber("canal", Int16, llamado)
    rospy.spin() 
if __name__=='__main__':
    print "Recibiendo Nodo"
    recibe()
