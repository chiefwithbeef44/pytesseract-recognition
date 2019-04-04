import cv2


def startCamera(camNum):
	"""
	Do NOT use this method.
	:return: returns the camera variable to get feed.
	"""
	cam = cv2.VideoCapture(camNum)
	return cam


def showCamera(camNum):
	while True:

		cam = startCamera(camNum)
		frame = cam.read()

		grayscaleImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow("cv", grayscaleImage)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cam.release()
	cv2.destroyAllWindows()