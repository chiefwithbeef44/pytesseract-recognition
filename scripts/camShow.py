import cv2

def startCamera(camNum):
	"""
	Do NOT use this method.
	:return: returns the camera variable to get feed.
	"""
	cam = cv2.VideoCapture(camNum)
	return cam

def showCamera(camNum):
	cam = startCamera(camNum)
	frame = cam.read()
	grayscaleImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow("cv", grayscaleImage)