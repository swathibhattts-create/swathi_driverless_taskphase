from setuptools import find_packages, setup

package_name = 'task2_nodes'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name],
        ),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='swathi',
    maintainer_email='swathi@todo.todo',
    description='ROS 2 palindrome checker task',
    license='Apache-2.0',
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'string_publisher = task2_nodes.string_publisher:main',
            'palindrome_checker = task2_nodes.palindrome_checker:main',
            'result_responder = task2_nodes.result_responder:main',
        ],
    },
)
