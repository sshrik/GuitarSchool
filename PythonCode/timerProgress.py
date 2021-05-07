import threading
import time

def show(p, t=3):
    while p.progressed != p.pMax:
        p.showProgress()
        time.sleep(t)
    p.showProgress()
    print("")

class Progress:
    '''
    To show how progressed.
    show [=======                ] with ( progressed/pMax )
    '''
    def __init__(self, pMax):
        self.pMax = pMax
        self.progressed = 0

    def showProgress(self):
        print('\r', end="")
        print('[', end="")
        prog = (int)((self.progressed * 100)/self.pMax)
        for i in range(0, 100):
            if i < prog:
                print("=", end="")
            else:
                print(" ", end="")
        print(']', end="")
        print(str(self.progressed) + " / " + str(self.pMax), end="")

    def setProgress(self, p):
        self.progressed = p

    def addProgress(self):
        self.progressed += 1

    def subProgress(self):
        self.progressed -= 1

    def showProgressTimer(self, wt=1):
        self.thr = threading.Thread(target=show, args=(self, wt))
        # If thr.join was called, then main will waiting with block-state when thread will finish.
        self.thr.start()

    def timerJoin(self):
        self.thr.join()
