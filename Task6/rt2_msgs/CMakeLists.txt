cmake_minimum_required(VERSION 3.5)
project(rt2_msgs)

find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/RT2String.msg"
)

ament_package()

