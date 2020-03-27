from multiprocessing import Queue, Process
from time import sleep

def download(q):
    images = ["girl.jpn","boy.jpg","man.jpg"]
    for image in images:
        print("Downloading: ", image)
        sleep(0.5)
        q.put(image)


def getfile(q):
    while True:
        try:
            file = q.get(timeout = 5)
            print("File {} has being saved".format(file))
        except:
            print("Done")
            break
     

if __name__ == "__main__":
    q = Queue(5)
    p1 = Process(target= download, args=(q,))
    p2 = Process(target= getfile, args=(q,))

    p1.start()
    p1.join()
    p2.start()
    p2.join()


