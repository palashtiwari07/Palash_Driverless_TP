import rclpy
from rclpy.node import Node
from task_one_msgs.msg import TaskOne

class TaskOnePublisher(Node):
    def __init__(self):
        super().__init__('taskone_publisher')
        self.publisher_ = self.create_publisher(TaskOne, '/taskone', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        angVel = float(input("Enter angular velocity (rad/s): "))
        radius = float(input("Enter radius (m): "))

        msg = TaskOne()
        msg.ang_vel = angVel
        msg.radius = radius

        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: angVel={angVel}, radius={radius}')

def main(args=None):
    rclpy.init(args=args)
    node = TaskOnePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
