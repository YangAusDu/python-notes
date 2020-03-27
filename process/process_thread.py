from multiprocessing import Queue, Process
import threading
from time import sleep

def download(q):
    images = ["girl.jpn","boy.jpg","man.jpg"]
    for image in images:
        print("Downloading: ", image)
        sleep(1.5)
        print("{} Downloaded ".format(image))


     
if __name__ == "__main__":
    t = threading.Thread(target=download, name = 'aa',args=(1,))
    t.start()

    n = 1
    while True:
        n += 1
        sleep(1.5)
        print(n)