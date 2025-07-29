import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    # Locate package paths
    iai_tiago_description_path = get_package_share_directory('iai_tiago_description')

    # File paths
    urdf_file = os.path.join(iai_tiago_description_path, 'urdf', 'tiago_dual.urdf')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': ParameterValue(open(urdf_file).read(), value_type=str),
            }]
        )
    ])
