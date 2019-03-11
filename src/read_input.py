#!/usr/bin/env python

import roslib
import rospy
import std_msgs.msg
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from ServoPi import PWM
import time
import math

pwm = PWM(0x40)
pwm.set_pwm_freq(50)

ts = 0.2

low = 205
mid = 307
high = 410

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.buttons)
	if data.buttons[0] == 1:
		pwm.set_pwm(1, 0, mid)
	if data.buttons[3] == 1:
		pwm.set_pwm(1, 0, low)
	if data.buttons[1] == 1:
		pwm.set_pwm(1, 0, high)

def listener():

	rospy.init_node('listener',anonymous=True)
	jsinput = rospy.Subscriber('/joy', Joy, callback)
	
	print jsinput

	rospy.spin()

if __name__ == '__main__':
	listener()
