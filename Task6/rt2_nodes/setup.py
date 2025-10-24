from setuptools import setup

package_name = 'rt2_nodes'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='palash',
    maintainer_email='palash@example.com',
    description='Three ROS2 nodes communicating using custom messages',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'node1_publisher = rt2_nodes.node1_publisher:main',
            'node2_palindrome_checker = rt2_nodes.node2_palindrome_checker:main',
            'node3_response = rt2_nodes.node3_response:main',
        ],
    },
)

