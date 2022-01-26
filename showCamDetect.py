import sys
import CameraDetection as cd
import cv2

n = len(sys.argv)
if n < 4:
	print "Wrong number of arguments"
	exit()
img = cv2.imread(sys.argv[1])
img = cv2.resize(img, (1008,756))
#shows image after filtered by hue
print cd.cameraHueView(img, float(sys.argv[2]), float(sys.argv[3]))
