import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
class FusionNode(Node):
    def __init__(self):
        super().__init__('fusion_node')
        self.vib=None; self.therm=None
        self.sub1=self.create_subscription(Float32,'/sensor/vibration',self.cb1,10)
        self.sub2=self.create_subscription(Float32,'/sensor/thermal',self.cb2,10)
        self.pub=self.create_publisher(Float32,'/sensor/fusion_score',10)
    def cb1(self,m): self.vib=m.data; self.fuse()
    def cb2(self,m): self.therm=m.data; self.fuse()
    def fuse(self):
        if self.vib is None or self.therm is None: return
        score=self.vib*0.6+(self.therm-25)*0.4
        self.pub.publish(Float32(data=score))
def main(args=None):
    rclpy.init(args=args)
    n=FusionNode(); rclpy.spin(n); rclpy.shutdown()
