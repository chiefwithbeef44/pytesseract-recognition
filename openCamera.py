import cv2

def getCamType():
	camera =input("Choose a camera: 0. Laptop Webcam 1. USB Webcam")
	if(camera == 0):
		return camera
	elif(camera == 1):
		return camera
	else:
		return 1


cam = cv2.VideoCapture(getCamType())

while True:

	frame = cam.read()
	colorImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	# Display the rgb frame
	colorScan = cv2.imshow("color camera", colorImage)

	grayscaleImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# display the grayscale image
	grayscaleScan = cv2.imshow("grayscale camera", grayscaleImage)