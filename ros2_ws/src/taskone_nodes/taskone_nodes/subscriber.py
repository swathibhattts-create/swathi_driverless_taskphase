
import rclpy
from rclpy.node import Node
from taskone_interfaces.msg import TaskOne


class WheelSubscriber(Node):

    def __init__(self):
        super().__init__('wheel_subscriber')

        self.subscription = self.create_subscription(
            TaskOne,
            '/taskone',
            self.listener_callback,
            10
        )

        self.get_logger().info('Waiting for wheel data...')

    def listener_callback(self, msg):
        speed = msg.ang_vel * msg.radius

        self.get_logger().info(
            f'Angular velocity: {msg.ang_vel:.2f} rad/s'
        )
        self.get_logger().info(
            f'Wheel radius: {msg.radius:.2f} m'
        )
        self.get_logger().info(
            f'Longitudinal speed: {speed:.2f} m/s'
        )


def main(args=None):
    rclpy.init(args=args)
    node = WheelSubscriber()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
