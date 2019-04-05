def getCamera():
	print "Please select a webcam"
	print "Your default camera is camera #0"
	print "0. Internal Webcam"
	print "1. USB Webcam"
	camera = input("Your selection: ")
	return int(camera)


def pickLanguage():
	lang = 0
	print "Select a language: "
	print "Your default language is: " + str(lang)
	print "0. English"
	print "1. French"
	input("Your selection: ")
	if lang == 1:
		return "fra"
	else:
		return "eng"
