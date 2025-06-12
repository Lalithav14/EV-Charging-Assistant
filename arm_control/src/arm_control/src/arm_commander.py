import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from std_srvs.srv import Trigger
class ArmCommander(Node):
    def __init__(self):
        super().__init__('arm_commander')
        self.cli_move=self.create_client(Trigger,'move_home')
        self.pose_pub=self.create_publisher(PoseStamped,'target_pose',10)
    def move_home(self):
        req=Trigger.Request()
        self.cli_move.call_async(req)
    def goto(self,pose):
        ps=PoseStamped(); ps.pose=pose; self.pose_pub.publish(ps)
def main(args=None):
    rclpy.init(args=args)
    n=ArmCommander(); rclpy.spin(n); n.destroy_node(); rclpy.shutdown()
