#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import math

PI = math.pi

"""
Fungsi ini akan memanggil fungsi move dan rotate sesuai
bentuk yang ingin kita buat.

Contoh :
Input Speed : 5
Input Length : 4
square/triangle? : square

akan membuat persegi dengan panjang sisi 4
"""
def create_shape(shape, speed, length):
    if shape == "square":
        angle = 90
        for i in range(4):
            move(speed,length)
            rotate(180 - angle)
        move(speed,length)

    elif shape == "triangle":
        angle = 60
        for i in range(3):
            move(speed,length)
            rotate(180 - angle)
        move(speed,length)        

"""
Fungsi move akan membuat turtle bergerak searah
garis lurus sepanjang sisinya.
Topic yang digunakan adalah /turtle1/cmd_vel
"""
def move(speed, length):
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    
    vel_msg.linear.x = abs(speed)
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    
    while not rospy.is_shutdown():

        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        while(current_distance < length):
            velocity_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec()
            current_distance= speed*(t1-t0)

        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)

        if current_distance >= length:
            break

"""
Fungsi rotate akan membuat turtle berbelok sebanyak
sudut yang diinginkan. Sudut dalam derajat.
Topic yang digunakan adalah /turtle1/cmd_vel
"""
def rotate(angle):
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    speed = angle

    angular_speed = speed*2*PI/360
    relative_angle = angle*2*PI/360

    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = abs(angular_speed)

    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)

    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    rospy.init_node('robot_move_turtle', anonymous=True)
    try:
        speed = input("Input Speed : ")
        length = input("Input Length : ")
        shape = raw_input("square/triangle? : ")
        create_shape(shape, speed, length)
        rospy.spin()
    except rospy.ROSInterruptException: 
        pass

