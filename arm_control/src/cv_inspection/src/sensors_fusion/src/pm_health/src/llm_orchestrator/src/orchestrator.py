import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger
import openai
class Orchestrator(Node):
    def __init__(self):
        super().__init__('orchestrator')
        self.srv=self.create_service(Trigger,'/inspect',self.cb)
        openai.api_key='YOUR_KEY'
    def cb(self,req,resp):
        cmd='Inspect battery port and evaluate health.'
        resp2=openai.ChatCompletion.create(model='gpt-4',messages=[{'role':'system','content':'robot master'},{'role':'user','content':cmd}])
        self.get_logger().info(resp2.choices[0].message.content)
        return resp
def main(args=None):
    rclpy.init()
    n=Orchestrator(); rclpy.spin(n); rclpy.shutdown()
