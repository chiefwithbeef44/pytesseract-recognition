import cv2
import scripts.__init__ as init

def startCamera():
	"""
	Do NOT use this method.
	:return: returns the camera variable to get feed.
	"""
	cam = cv2.VideoCapture(init.getCamera())
	return cam

def showCamera():
	startCamera()
