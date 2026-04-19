import rclpy
from geometry_msgs.msg import Twist

class SimSerialRobot:
    def __init__(self, node):
        self.node = node
        self.pub = node.create_publisher(Twist, "/cmd_vel", 10)

    def move_forward(self, speed=0.2):
        msg = Twist()
        msg.linear.x = speed
        self.pub.publish(msg)

    def rotate(self, angular=0.5):
        msg = Twist()
        msg.angular.z = angular
        self.pub.publish(msg)

    def stop(self):
        self.pub.publish(Twist())

