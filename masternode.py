import rospy
import string
#from std_msgs.msg import String

from sensor_msgs.msg import PointCloud2
#import std_msgs.msg
#import sensor_msgs.point_cloud2 as pcl2
class Server:
	def __init__(self):
		self.laser_data = None
		self.image_data = None
	def laser_callback(self,msg):
		self.laser_data = msg
		self.overlap()
	def image_callback(self,msg):
	        self.image_data = msg
	def overlap(self):
		#if self.image_data is not None and self.laser_data is not None:
		if self.laser_data is not None:
		#desired operation here
			print("Hello world")

def projection():
	rospy.init_node('projection', anonymous=True)
	server = Server()
	rospy.Subscriber("/lidar_left/velodyne_points", PointCloud2, server.laser_callback)
	#rospy.Subscriber("/front_camera/image_raw", Image, server.image_callback)
	rospy.spin()

if __name__ == '__main__':
	projection()
