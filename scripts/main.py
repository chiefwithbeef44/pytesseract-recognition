import pytesseract
import cv2


def main(camNum, lang):

	cam = cv2.VideoCapture(camNum)

	while True:
		ret, frame = cam.read()

		grayscaleImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		output = pytesseract.image_to_string(grayscaleImage, lang=lang, nice=0, output_type=pytesseract.Output.STRING)
		boxes = pytesseract.image_to_boxes(grayscaleImage)

		if(output != ""):
			print output
			print "------------------------------------------------------------"