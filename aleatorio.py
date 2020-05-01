#!/usr/bin/env python
import rospy
import random
from std_msgs.msg import Int16 
def aleatorio():
     pub = rospy.Publisher('canal' , Int16, queue_size=10)
     rospy.init_node('ale', anonymous=True)
     fre=rospy.Rate(0.5) #frecuencia
     print "nodo creado con exito"
     while not rospy.is_shutdown():
        num =(random.randrange(1000)) #% rospy.get_time()
        rospy.loginfo(num)
        pub.publish(num)
        fre.sleep()
if __name__=='__main__':
     try:
        aleatorio()
     except rospy.ROSInterruptException:
        pass


