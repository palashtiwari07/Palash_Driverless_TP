import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from rt2_msgs.msg import RT2String

class Node3Response(Node):
    def __init__(self):
        super().__init__('node3_response')
        self.subscriber_ = self.create_subscription(Int32, 'palindrome_result', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(RT2String, 'response_topic', 10)
        self.get_logger().info('Node3 Response started')

    def listener_callback(self, msg):
        response = RT2String()
        response.data = "Yes" if msg.data == 1 else "No"
        self.publisher_.publish(response)
        self.get_logger().info(f'Received {msg.data}, Responded: "{response.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = Node3Response()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
