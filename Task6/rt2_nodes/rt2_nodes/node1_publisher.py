import rclpy
from rclpy.node import Node
from rt2_msgs.msg import RT2String

class Node1Publisher(Node):
    def __init__(self):
        super().__init__('node1_publisher')
        self.publisher_ = self.create_publisher(RT2String, 'string_topic', 10)
        self.timer = self.create_timer(2.0, self.timer_callback)
        self.get_logger().info('Node1 Publisher started')

    def timer_callback(self):
        user_input = input("Enter a string: ")
        msg = RT2String()
        msg.data = user_input
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = Node1Publisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
