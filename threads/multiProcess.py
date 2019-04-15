from scripts import camShow as cvShow, utilities as init, tesseract as runner
from multiprocessing import process

cvShow.defaultCam = init.getCamera()
lang = init.pickLanguage()

tesseractProcess = process.Process(target=runner.main(lang, cvShow.defaultCam))
tesseractProcess.daemon = True

cameraProcess = process.Process(target=cvShow.show())
cameraProcess.daemon = True

if __name__ == '__main__':
	cameraProcess.start()
	tesseractProcess.start()
