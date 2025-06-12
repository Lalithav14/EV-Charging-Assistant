# launch/full_system_launch.py

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='arm_control', executable='arm_commander', output='screen'),
        Node(package='cv_inspection', executable='inspection_node', output='screen'),
        Node(package='sensors_fusion', executable='fusion_node', output='screen'),
        Node(package='pm_health', executable='health_node', output='screen'),
        Node(package='llm_orchestrator', executable='orchestrator', output='screen'),
    ])
