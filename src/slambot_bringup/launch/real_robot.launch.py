import os
from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch_ros.actions import Node


def generate_launch_description():
    use_slam = LaunchConfiguration("use_slam")

    use_slam_arg = DeclareLaunchArgument("use_slam", default_value="true")

    hardware_interface = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("slambot_firmware"),
            "launch",
            "hardware_interface.launch.py",
        )
    )

    controller = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("slambot_controller"),
            "launch",
            "controller.launch.py",
        ),
        # launch_arguments={"use_diffdrive_controller":"True"}.items()
    )

    joystick = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("slambot_controller"),
            "launch",
            "joystick_teleop.launch.py",
        )
    )

    slam = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("slambot_controller"),
            "launch",
            "online_async_launch.py",
        ),
        condition=IfCondition(use_slam),
    )
    camera = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("slambot_bringup"),
            "launch",
            "camera_web.launch.py",
        )
    )

    # camera_publisher=Node(
    #     package="slambot_camera",
    #     executable="camera_pub"
    # )

    return LaunchDescription(
        [
            use_slam_arg,
            hardware_interface,
            controller,
            joystick,
            slam,
            # camera_publisher
        ]
    )
