from pytesseract import *
import cv2
import time

cam = cv2.VideoCapture(0)

while True:
	ret, frame = cam.read()

	grayscaleImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# display the grayscale image
	cv2.imshow("grayscale camera", grayscaleImage)

	output = pytesseract.image_to_string(grayscaleImage, lang="eng", nice=0, output_type=pytesseract.Output.STRING)
	boxes = pytesseract.image_to_boxes(grayscaleImage)

	if(output != ""):
		print output, pytesseract.get_errors("")
		print "------------------------------------------------------------"

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cam.release()
cv2.destroyAllWindows()
