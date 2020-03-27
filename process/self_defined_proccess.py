from multiprocessing import Process

class MyProcess(Process):

    def __init__(self,name):
        super(MyProcess,self).__init__()
        self.name = name
        

    def run(self):
        p = 1
        while True:
            print("{}--------->self-defined, p: {}".format(self.name, p))
            p +=1 

if __name__ == "__main__":
    p1 = MyProcess("Shirely")
    p2 = MyProcess("Lucy")
    p1.start()
    p2.start()