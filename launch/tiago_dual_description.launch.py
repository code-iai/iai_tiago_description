import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    iai_tiago_description_path = get_package_share_directory('iai_tiago_description')
    upload_launch = os.path.join(iai_tiago_description_path, 'robots', 'upload.launch.py')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(upload_launch)
        )
    ])
