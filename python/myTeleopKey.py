import termios, sys, os
import rospy
from turtlesim.srv import TeleportAbsolute, TeleportRelative
import argparse
from geometry_msgs.msg import Twist 
from turtlesim.msg import Pose
import math

TERMIOS = termios

def get_key():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c

def teleport_absolute(x, y, ang):
    rospy.wait_for_service('/turtle1/teleport_absolute')
    try:
        teleportA = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
        resp1 = teleportA(x, y, ang)
        print('Teleported to x: {}, y: {}, ang: {}'.format(str(x),str(y),str(ang)))
    except rospy.ServiceException as e:
        print(str(e))

def teleport_relative(linear, ang):
    rospy.wait_for_service('/turtle1/teleport_relative')
    try:
        teleportA = rospy.ServiceProxy('/turtle1/teleport_relative', TeleportRelative)
        resp1 = teleportA(linear, ang)
    except rospy.ServiceException as e:
        print(str(e))

def pubVel(vel_x, ang_z, t):
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('velPub', anonymous=False)
    vel = Twist()
    vel.linear.x = vel_x
    vel.angular.z = ang_z
    #rospy.loginfo(vel)
    endTime = rospy.Time.now() + rospy.Duration(t)
    while rospy.Time.now() < endTime:
        pub.publish(vel)

if __name__ == "__main__":
    while True:
        key = get_key()
        if key == b'q':
            break
        elif key == b'w':
            pubVel(1, 0, 0.01)
        elif key == b's':
            pubVel(-1, 0, 0.01)
        elif key == b'd':
            pubVel(0, -1, 0.01)
        elif key == b'a':
            pubVel(0, 1, 0.01)
        elif key == b'r':
            teleport_absolute(5.544444561004639,5.544444561004639,0)
        elif key == b' ':
            teleport_relative(0,math.pi)
