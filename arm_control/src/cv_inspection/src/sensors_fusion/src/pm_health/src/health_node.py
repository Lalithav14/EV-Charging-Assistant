import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import joblib
class HealthNode(Node):
    def __init__(self):
        super().__init__('health_node')
        self.model=joblib.load('models/pm_xgb.pkl')
        self.sub=self.create_subscription(Float32,'/sensor/fusion_score',self.cb,10)
        self.pub=self.create_publisher(Float32,'/health/rul',10)
    def cb(self,m):
        rul=float(self.model.predict([[m.data]]))
        self.pub.publish(Float32(data=rul))
def main(args=None):
    rclpy.init()
    n=HealthNode(); rclpy.spin(n); rclpy.shutdown()
