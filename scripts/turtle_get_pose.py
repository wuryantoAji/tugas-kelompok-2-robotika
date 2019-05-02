#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose
import time

def callback(pose):
    rospy.loginfo(rospy.get_caller_id() + '\nPosisi x : %.2f\nPosisi y : %.2f' % (pose.x, pose.y))
    

"""
Fungsi ini digunakan untuk melakukan subscribe posisi turtle.
Topic yang digunakan adalah /turtle1/pose
"""
def listener():

    rospy.init_node('robot_listener', anonymous=True)

    rospy.Subscriber('/turtle1/pose', Pose, callback)

    # Biarkan program berjalan hingga di stop
    rospy.spin()

if __name__ == '__main__':
    listener()

