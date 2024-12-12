from launch_ros.actions import Node
from launch import LaunchDescription


def generate_launch_description():
    camera_publisher = Node(package="slambot_camera", executable="camera_pub")

    web_pub = Node(package="web_video_server", executable="web_video_server")

    return LaunchDescription([camera_publisher, web_pub])
