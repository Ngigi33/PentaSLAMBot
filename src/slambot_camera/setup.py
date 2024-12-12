from setuptools import find_packages, setup

package_name = 'slambot_camera'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='strawhat',
    maintainer_email='strawhat@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['camera_pub=slambot_camera.camera_publisher:main',
                            'camera_sub=slambot_camera.camera_subscriber:main',
        ],
    },
)
