
# Default is internal camera
camera = 0

#Gets what camera the user would like to use
def getCamera():
	print "Please select a webcam"
	print "Your default camera is camera #"+camera
	print "0. Internal Webcam"
	print "1. USB Webcam"
	input("Your selection: ", camera)
	return camera

if __name__ == "__init__":
	getCamera()