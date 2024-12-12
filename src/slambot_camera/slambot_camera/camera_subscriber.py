import cv2 
import rclpy 
from sensor_msgs.msg import Image
from rclpy.node import Node
from cv_bridge import CvBridge

class CameraSubscriber(Node):

    def __init__(self):
        super().__init__("camera_subscriber_node")
        self.bridge_Object=CvBridge() #convert to Ros image messages from opencv images
        self.sub_=self.create_subscription(Image,"slambot/camera_images",self.camera_listener_callback,20)
        

    def camera_listener_callback(self,image_msg):
        self.get_logger().info("Received Image Frame")
        openCVImage=self.bridge_Object.imgmsg_to_cv2(image_msg)#convert ros message to opencv image
        cv2.imshow("CAMERA video",openCVImage)
        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args=args)
    node=CameraSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

