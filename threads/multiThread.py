import scripts.main as runner
from scripts import initScripts as init
import scripts.camShow as cvShow
import threading

camera = init.getCamera()
lang = init.pickLanguage()

tessThread = threading.Thread(runner.main(camera, lang))
camThread = threading.Thread(cvShow.showCamera(camera))

if __name__ == '__main__':
	camThread.start()
	tessThread.start()