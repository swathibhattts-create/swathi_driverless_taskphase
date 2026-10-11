
import rclpy
from rclpy.node import Node
from taskone_interfaces.msg import TaskOne


class WheelPublisher(Node):

    def __init__(self):
        super().__init__('wheel_publisher')
        self.publisher_ = self.create_publisher(
            TaskOne, '/taskone', 10
        )

    def publish_data(self, ang_vel, radius):
        msg = TaskOne()
        msg.ang_vel = ang_vel
        msg.radius = radius
        self.publisher_.publish(msg)
        self.get_logger().info(
            f'Published ang_vel={ang_vel}, radius={radius}'
        )



def main(args=None):
    rclpy.init(args=args)
    node = WheelPublisher()

    try:
        ang_vel = float(input('Enter angular velocity (rad/s): '))
        radius = float(input('Enter wheel radius (m): '))

        while rclpy.ok():
            node.publish_data(ang_vel, radius)
            rclpy.spin_once(node, timeout_sec=0.5)

    except ValueError:
        node.get_logger().error('Enter valid numerical values.')
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
