import rclpy
from rclpy.node import Node
from rt2_msgs.msg import RT2String
from std_msgs.msg import Int32

class Node2PalindromeChecker(Node):
    def __init__(self):
        super().__init__('node2_palindrome_checker')
        self.subscriber_ = self.create_subscription(RT2String, 'string_topic', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(Int32, 'palindrome_result', 10)
        self.response_sub_ = self.create_subscription(RT2String, 'response_topic', self.response_callback, 10)
        self.get_logger().info('Node2 Palindrome Checker started')

    def listener_callback(self, msg):
        s = msg.data
        if s == s[::-1]:
            is_palindrome = 1
        else:
            is_palindrome = 0
        out = Int32()
        out.data = is_palindrome
        self.publisher_.publish(out)
        self.get_logger().info(f'Received "{s}", Palindrome: {bool(is_palindrome)}')

    def response_callback(self, msg):
        self.get_logger().info(f'Node3 responded: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = Node2PalindromeChecker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
