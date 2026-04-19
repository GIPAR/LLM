import rclpy
from controller.robot_controller import RobotController
from model.llm_model import LLMModel
from ros_interface.sim_serial_robot import SimSerialRobot
from view.user_view import UserView

def main():
    rclpy.init()

    node = rclpy.create_node("llm_sim_serial")
    view = UserView()
    llm = LLMModel()

    robot = SimSerialRobot(node)
    controller = RobotController(llm, None, view, robot)

    try:
        while rclpy.ok():
            controller.run()
            rclpy.spin_once(node, timeout_sec=0.1)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

