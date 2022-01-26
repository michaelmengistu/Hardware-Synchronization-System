import rosbag
import pypcd
import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import PointCloud2
import CameraDetection as cd
import numpy as np
import sys

from GravityPhysics import *

def validate(bagFile, timeA, timeB):
	#takes in bag file and the time range at which the error will be calculated
	t0 = rospy.Time(timeA).to_sec()
	t1 = rospy.Time(timeB).to_sec()
	bag = rosbag.Bag(bagFile)

	img_msgs =  bag.read_messages(topics=['/front_camera/image_raw', '/lidar_left/velodyne_points'])

	bridge = CvBridge()
    
	lidarH = []
	cameraH = []
	#loops through messages
	for topic, msg, t in img_msgs:
		if t.to_sec() >= t0 and t.to_sec() <= t1 and topic == '/front_camera/image_raw':
			cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
			cv_image = cv2.resize(cv_image, (800, 600))
			#gets camera y pos (using ground pixel position and pixel drop height and height droped in meters) then hue values
            		var = (cd.cameraFindObj(cv_image, 250, 450, 2, 150, 170), t.to_sec())
            		cameraH.append(var)
		if topic == '/lidar_left/velodyne_points' and t.to_sec() >= t0 and t.to_sec() <= t1:	
			pc = pypcd.PointCloud.from_msg(msg)
			#gets lidar with bouding cords x, y, z (z should be height) and then the height droped from (in z cords)
			var = (cd.lidarFindObj(pc, 6.85, 6.95,3.70, 3.95,-2.3,0,0),t.to_sec())
            		lidarH.append(var)
		
	bag.close()
    
	timeD = np.zeros(min(len(lidarH), len(cameraH)))
	i = 0
	#loops through objects found and gets time error between them pairing one to one
	for x,y in zip(lidarH,cameraH):
		if(x[0] == -1 or y[0] == -1):
			continue #skips any data where an object was not found	
		diff = timeDiff(x[0],y[0])
		
		#accounts for the difference in the labeled timestamps
		labeledDiff = abs(x[1] - y[1])
		diff = abs(diff - labeledDiff) 

		timeD[i] = diff
		i+=1
	print("mean: ", np.mean(timeD))
	print("standard deviation: ", np.std(timeD))


n = len(sys.argv)
if n < 4:
	print "Wrong number of arguments"
	exit()
validate(sys.argv[1], float(sys.argv[2]), float(sys.argv[3]))




