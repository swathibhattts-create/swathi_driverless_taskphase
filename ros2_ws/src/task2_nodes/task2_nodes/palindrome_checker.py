import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String
from task2_interfaces.msg import RT2String


class PalindromeChecker(Node):
    def __init__(self):
        super().__init__('palindrome_checker')

        self.result_publisher = self.create_publisher(
            Int32, '/palindrome_result', 10
        )

        self.string_subscriber = self.create_subscription(
            RT2String,
            '/input_string',
            self.check_palindrome,
            10
        )

        self.response_subscriber = self.create_subscription(
            String,
            '/text_response',
            self.receive_response,
            10
        )

    def check_palindrome(self, msg):
        text = msg.data
        result = Int32()

        if text == text[::-1]:
            result.data = 1
        else:
            result.data = 0

        self.get_logger().info(
            f'Input: {text}, Result: {result.data}'
        )

        self.result_publisher.publish(result)

    def receive_response(self, msg):
        self.get_logger().info(f'Final answer: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = PalindromeChecker()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
