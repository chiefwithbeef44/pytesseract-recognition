import cv2

global cam
global grayscaleImage
defaultCam = 0


def getCamera(camNum):
	defaultCam = camNum
	cam = cv2.VideoCapture(camNum)
	return cam


def show():
	while True:
		cam = cv2.VideoCapture(defaultCam)
		frame = cam.read()

		grayscaleImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow("cv", grayscaleImage)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cam.release()
	cv2.destroyAllWindows()