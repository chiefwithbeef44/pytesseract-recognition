from pytesseract import *
import cv2
from PIL import Image

cam = cv2.VideoCapture(1)


def getImage(bytes):
	return Image.fromarray(bytes)


while True:

	ret, frame = cam.read()
	colorImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	# Display the rgb frame
	colorScan = cv2.imshow("color camera", colorImage)

	grayscaleImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# display the grayscale image
	grayscaleScan = cv2.imshow("grayscale camera", grayscaleImage)

	tessFeed = pytesseract.image_to_boxes(grayscaleImage)

	output = pytesseract.image_to_string(grayscaleImage)
	if(output == ""):
		print "nothing seen"
	else:
		print output, tessFeed

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cam.release()
cv2.destroyAllWindows()