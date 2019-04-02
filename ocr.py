from tesserocr import PyTessBaseAPI
from pytesseract import *
import cv2
from PIL import Image

cam = cv2.VideoCapture(1)


def getImage(bytes):
	return Image.fromarray(bytes)


while True:

	ret, frame = cam.read()
	colorImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	# Display the resulting frame
	scan = cv2.imshow("webcam", colorImage)

	grayscaleImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	tessFeed = pytesseract.image_to_boxes(colorImage)
	print pytesseract.image_to_string(colorImage)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cam.release()
cv2.destroyAllWindows()