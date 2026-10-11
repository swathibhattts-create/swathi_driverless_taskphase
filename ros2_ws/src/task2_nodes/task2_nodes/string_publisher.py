import rclpy
from rclpy.node import Node
from task2_interfaces.msg import RT2String


class StringPublisher(Node):
    def __init__(self):
        super().__init__('string_publisher')

        self.publisher_ = self.create_publisher(
            RT2String, '/input_string', 10
        )

        self.text = input('Enter a string: ')
        self.timer = self.create_timer(1.0, self.publish_string)

    def publish_string(self):
        msg = RT2String()
        msg.data = self.text

        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = StringPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
