import cv2


# noinspection PyPep8Naming
def getCamera(camNum):
	global defaultCam
	defaultCam = camNum
	return defaultCam


def show():
	cam = cv2.VideoCapture(defaultCam)

	while True:
		ret, frame = cam.read()

		# noinspection PyPep8Naming
		grayscaleImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow("image", grayscaleImage)

		if cv2.waitKey(1) & 0xFF == ord("q"):
			break

	cam.release()
	cv2.destroyAllWindows()