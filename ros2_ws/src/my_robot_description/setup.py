import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'my_robot_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='thomas',
    maintainer_email='thomas@todo.todo',
    description='URDF description, launch and RViz config for a '
                'differential-drive robot with a front caster wheel.',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'wheel_publisher = my_robot_description.wheel_publisher:main',
        ],
    },
)
