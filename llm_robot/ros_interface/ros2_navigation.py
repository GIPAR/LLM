import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import PoseStamped
import math

class Nav2Navigation(Node):
    def __init__(self):
        super().__init__("llm_nav2_client")
        self.client = ActionClient(self, NavigateToPose, "navigate_to_pose")

    def send_goal(self, x: float, y: float, theta: float = 0.0):
        while not self.client.wait_for_server(timeout_sec=2.0):
            self.get_logger().info("Aguardando Nav2...")

        goal = NavigateToPose.Goal()
        goal.pose = PoseStamped()
        goal.pose.header.frame_id = "map"
        goal.pose.header.stamp = self.get_clock().now().to_msg()

        goal.pose.pose.position.x = x
        goal.pose.pose.position.y = y

        # yaw → quaternion
        goal.pose.pose.orientation.z = math.sin(theta / 2.0)
        goal.pose.pose.orientation.w = math.cos(theta / 2.0)

        self.client.send_goal_async(goal)
