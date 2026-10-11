from setuptools import find_packages, setup

package_name = 'taskone_nodes'

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
    maintainer='swathi',
    maintainer_email='swathi@example.com',
    description='ROS 2 publisher and subscriber for wheel speed',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = taskone_nodes.publisher:main',
            'subscriber = taskone_nodes.subscriber:main',
        ],
    },
)
