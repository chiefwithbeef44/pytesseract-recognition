import cv2

global defaultCam
defaultCam = 0


def getCamera(camNum):
	defaultCam = camNum
	return defaultCam


def show():
	cam = cv2.VideoCapture(defaultCam)

	while True:
		ret, frame = cam.read()

		# noinspection PyPep8Naming
		grayscaleImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow(cv2.namedWindow("cv", cv2.WINDOW_NORMAL), grayscaleImage)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cam.release()
	cv2.destroyAllWindows()