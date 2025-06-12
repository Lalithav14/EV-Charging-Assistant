# cv_inspection/src/inspection_node.py

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class InspectionNode(Node):
    def __init__(self):
        super().__init__('inspection_node')
        self.subscription = self.create_subscription(
            Image, '/camera/image_raw', self.image_callback, 10)
        self.bridge = CvBridge()
        self.get_logger().info('CV Inspection Node started.')

    def image_callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        cv2.imshow('Detected Edges', edges)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = InspectionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
