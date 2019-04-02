from tesserocr import PyTessBaseAPI as api
import cv2
from PIL import Image

cam = cv2.VideoCapture(1)


def getImage(bytes):

	image = Image.fromstring('RGB', (640, 480), bytes)
	return image


while True:

	ret, frame = cam.read()
	color = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	print color
	# Display the resulting frame
	scan = cv2.imshow('frame', color)

	api.SetImageFile(getImage(scan))
	print api.GetUTF8Text()
	print api.AllWordConfidences()

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cam.release()
cv2.destroyAllWindows()
