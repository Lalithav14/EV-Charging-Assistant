import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import torch
class InspectionNode(Node):
    def __init__(self):
        super().__init__('inspection_node')
        self.sub=self.create_subscription(Image,'/camera/image_raw',self.process,10)
        self.pub=self.create_publisher(Image,'/cv/annotated',10)
        self.bridge=CvBridge()
        self.model=torch.hub.load('ultralytics/yolov5','custom',path='models/ev_yolo.pt',force_reload=False)
    def process(self,msg):
        img=self.bridge.imgmsg_to_cv2(msg,'bgr8')
        res=self.model(img)
        annotated=res.render()[0]
        out=self.bridge.cv2_to_imgmsg(annotated,'bgr8')
        self.pub.publish(out)
def main(args=None):
    rclpy.init(args=args)
    n=InspectionNode(); rclpy.spin(n); n.destroy_node(); rclpy.shutdown()
