from setuptools import setup

package_name = 'task_one_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name] if 'resource' in package_name else []),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='palash',
    maintainer_email='palash@example.com',
    description='Publisher and subscriber for TaskOne custom message',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher_node = task_one_pkg.publisher_node:main',
            'subscriber_node = task_one_pkg.subscriber_node:main',
        ],
    },
)
