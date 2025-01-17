from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument , SetEnvironmentVariable , IncludeLaunchDescription
import os
from ament_index_python.packages import get_package_share_directory , get_package_prefix
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command , LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource 

def generate_launch_description():
    
    model_arg=DeclareLaunchArgument(
        name="model",
        default_value=os.path.join(get_package_share_directory("slambot_description"),"urdf","pentaslam.urdf.xacro"),
        description="Absolute path to robot URDF file"
    )
    robot_description= ParameterValue(Command(["xacro ", LaunchConfiguration("model")]),value_type=str)
    # robot_description= ParameterValue(Command([ LaunchConfiguration("model")]),value_type=str)
    
    # robot_state_publisher=Node(
    #     package="robot_state_publisher",
    #     executable="robot_state_publisher",
    #     parameters=[{"robot_description":robot_description, 'use_sim_time':True}]
    # )
    
    robot_state_publisher=Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description":robot_description,}]
    )
    
    env_var= SetEnvironmentVariable("GAZEBO_MODEL_PATH",os.path.join(get_package_prefix("slambot_description"),"share"))
    
    start_gazebo_server=IncludeLaunchDescription(PythonLaunchDescriptionSource(
        os.path.join(get_package_share_directory("gazebo_ros"),"launch","gzserver.launch.py")
    ))
    start_gazebo_client=IncludeLaunchDescription(PythonLaunchDescriptionSource(
        os.path.join(get_package_share_directory("gazebo_ros"),"launch","gzclient.launch.py")
    ))
    
    
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch'), '/gazebo.launch.py']),
        )
    
    
    spawn_robot=Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-entity","slambot","-topic","robot_description"],
        parameters=[{'timeout': 60}],
        output="screen"
    )
    
    return LaunchDescription([
        # gazebo,
        
        model_arg,
        env_var,
        robot_state_publisher,
        start_gazebo_server,
        start_gazebo_client,
        spawn_robot
    ])