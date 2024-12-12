import cv2 
import rclpy 
from sensor_msgs.msg import Image
from rclpy.node import Node
from cv_bridge import CvBridge

class CameraPublisher(Node):

    def __init__(self):
        super().__init__("camera_publisher_node")

        #device number
        self.cam_number=0
        self.camera=cv2.VideoCapture(self.cam_number)

        self.bridge_Object=CvBridge() #convert to Ros image messages from opencv images

        #created publisher to publish message of type Image to topic slambot/camera_images  with queue size 20
        self.pub_=self.create_publisher(Image,"slambot/camera_images",20)

        #create timer 
        self.timer =self.create_timer(0.02, self.camera_reader_timer_callback)
        self.i=0 #image counter storage

    def camera_reader_timer_callback(self):
        success,frame=self.camera.read() #read frame from camera
        frame=cv2.resize(frame,(820,640), interpolation = cv2.INTER_CUBIC)

        if success == True:
            ros_msg=self.bridge_Object.cv2_to_imgmsg(frame,encoding="bgr8")#convert to ros image with bgr8 encoding for website viewing
            self.pub_.publish(ros_msg)

        self.get_logger().info("IMAGE NO = %d" %self.i)
        self.i=self.i+1

def main(args=None):
    rclpy.init(args=args)
    node=CameraPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

