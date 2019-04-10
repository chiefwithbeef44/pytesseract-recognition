import pytesseract
import cv2


def main(lang, cam):
	cam = cv2.VideoCapture(cam)
	while True:
		ret, frame = cam.read()

		# noinspection PyPep8Naming
		grayscaleImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		output = pytesseract.image_to_string(grayscaleImage, lang=lang, nice=0, output_type=pytesseract.Output.STRING)

		if output != "":
			print output
			print "------------------------------------------------------------"
