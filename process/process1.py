from time import sleep
from multiprocessing import Process
import os



#they don't share list1

def task1(time, name):
    global m
    #global list1
    while True:
        sleep(time)
        m+=1
        list1.append(str(m)+"task1")
        print("This is task1", m, list1)

def task2(time, name):
    global m
    #global ist1
    while True:
        sleep(time)
        m+=1
        list1.append(str(m)+"task2")
        print("This is task2", m, list1)

if __name__ == "__main__":
    m = 0
    list1 = []      
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