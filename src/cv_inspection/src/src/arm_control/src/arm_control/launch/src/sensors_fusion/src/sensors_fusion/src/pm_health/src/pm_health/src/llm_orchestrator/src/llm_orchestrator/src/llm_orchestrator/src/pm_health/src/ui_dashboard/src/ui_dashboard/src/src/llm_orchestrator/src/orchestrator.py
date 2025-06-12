import rclpy
from rclpy.node import Node
import openai
from std_msgs.msg import String

class LLMOrchestrator(Node):
    def __init__(self):
        super().__init__('orchestrator')
        self.subscription = self.create_subscription(String, 'vehicle_health_status', self.respond, 10)
        openai.api_key = 'your-openai-key'

    def respond(self, msg):
        prompt = f"The vehicle health status is: {msg.data}. Suggest actions."
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
        )
        answer = response.choices[0].message.content
        self.get_logger().info(f"LLM Response: {answer}")

def main(args=None):
    rclpy.init(args=args)
    node = LLMOrchestrator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
