from time import sleep
from multiprocessing import Process
import os

def task1(time, name):
    while True:
        sleep(time)
        print("This is {}".format(name) ,os.getpid(),"---------",os.getppid())  #get process id; get parent process id
    

def task2(time, name):
    while True:
        sleep(time)
        print("This is {}".format(name), os.getpid(),"---------",os.getppid())

if __name__ == "__main__":
    p1 = Process(target = task1, name = "Name: Task1",args=(1,"aa"))    

    p2 = Process(target = task2, name="Name: Task2",args=(2,"bb"))
    p1.start()
    print(p1.name)
    p2.start()
    print(p2.name)
    sleep(10)
    p1.terminate()
    p2.terminate()
    print("process terminated!!")

    #task1()
    #task2()
