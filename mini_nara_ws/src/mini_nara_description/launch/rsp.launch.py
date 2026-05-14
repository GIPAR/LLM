import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import xacro

def generate_launch_description():

    pkg_name = 'mini_nara_description'
    file_subpath = 'urdf/mini_nara.urdf.xacro'
    xacro_file = os.path.join(get_package_share_directory(pkg_name), file_subpath)
    
    # Converte o Xacro para XML
    robot_description_raw = xacro.process_file(xacro_file).toxml()

    # 1. Nó que publica a árvore do robô
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_raw}]
    )

    # 2. Nó que abre a janelinha para você girar as rodas manualmente
    node_joint_state_publisher_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        output='screen'
    )

    # 3. Nó que abre o visualizador 3D
    node_rviz = Node(
        package='rviz2',
        executable='rviz2',
        output='screen'
    )

    return LaunchDescription([
        node_robot_state_publisher,
        node_joint_state_publisher_gui,
        node_rviz
    ])