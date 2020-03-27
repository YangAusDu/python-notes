import threading
import random
import time

lock = threading.Lock()

list1= [0]*10

def task1():
    lock.acquire()
    for i in range(len(list1)):
        list1[i] = 1
        time.sleep(0.5)
    lock.release()

def task2():
    lock.acquire()
    for i in range(len(list1)):
        print("----------->",list1[i])
        time.sleep(0.5)
    lock.release()