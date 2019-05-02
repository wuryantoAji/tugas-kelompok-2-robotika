#! /usr/bin/env python
 
import rospy
from sensor_msgs.msg import LaserScan
 

laser_Region = []

def clbk_laser(msg):
    # 720/5 = 144
    global laser_Region
     regions = [
      min(min(msg.ranges[0:143]), 10),
      min(min(msg.ranges[144:287]), 10),
      min(min(msg.ranges[288:431]), 10),
      min(min(msg.ranges[432:575]), 10),
      min( min(msg.ranges[576:713]), 10),
     ]
    laser_Region = region
    rospy.loginfo(regions)

def check_range():
	for(i in laser_Region):
		if(i < 2):
			rotate()

def move():
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    
    vel_msg.linear.x = abs(2)
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
def rotate():
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    

    angular_speed = 90*2*PI/360
    relative_angle = 90*2*PI/360

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



def main():
    rospy.init_node('reading_laser')
    sub= rospy.Subscriber("/m2wr/laser/scan", LaserScan, clbk_laser)
    move()
    check_range()
    rospy.spin()
 
if __name__ == '__main__':
    main()
