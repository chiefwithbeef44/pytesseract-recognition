import scripts.tesseract as runner
from scripts import initScripts as init
import scripts.camShow as cvShow
import threading

camera = init.getCamera()
lang = init.pickLanguage()

tessThread = threading.Thread(target=runner.main(lang=lang, cam=cvShow.getCamera(camera)))
tessThread.daemon = True

cameraThread = threading.Thread(target=cvShow.show())
cameraThread.daemon = True

if __name__ == '__main__':
	tessThread.start()
	cameraThread.start()