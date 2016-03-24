from pyautogui import *
from PIL import ImageGrab as ig
from threading import *
from Queue import *
import time

leftx = 506
rightx = 755
y = 320

searchdist = 1

y = y - searchdist // 2

img = ig.grab().load()
right = img[rightx, y]
left = img[leftx, y]

side = 0

queue = Queue()

#Thread for grabbing images and adding them to the queue
def grabThread():
    while True:
        img = ig.grab()
        queue.put_nowait(img.load())

def testThread():
    side = 0
    try:
        while True:
            img = queue.get_nowait()
            if side == 0:
                if not img[leftx, y] == left:
                    press('right')
                    side = 1
                else:
                    press('left')
            else:
                if not img[rightx, y] == right:
                    press('left')
                    side = 0
                else:
                    press('right')
            time.sleep(0.25)
    except Empty:
        pass

def play():
    side = 0
    while True:
        try:
            nimg = ig.grab()
            img = nimg.load()
            if side == 0:
                if not img[leftx, y] == left:
                    press('right')
                    side = 1
                else:
                    press('left')
            else:
                if not img[rightx, y] == right:
                    press('left')
                    side = 0
                else:
                    press('right')
            time.sleep(0.33)
        except KeyboardInterrupt:
            break    

play()
'''for i in range(5):
    thread = Thread(target=grabThread)
    thread.daemon = True
    thread.start()     
for i in range(1): #Number of threads
    thread = Thread(target=testThread)
    thread.daemon = True
    thread.start()'''
