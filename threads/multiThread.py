import scripts.main as runner
import scripts.camShow as cam
import threading

tessThread = threading.Thread(runner.main())
camThread = threading.Thread(cam.showCamera())

if __name__ == '__main__':
	camThread.start()
	tessThread.start()