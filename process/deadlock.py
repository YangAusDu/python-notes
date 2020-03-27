from threading import Thread, Lock
import time

#Don't make a dead lock, it is something we should prevent
# use timeout attribute in lock
lock1 = Lock()
lock2 = Lock()

class MyThread(Thread):
    def run(self):
        if lock1.acquire():
            print(self.name, "lock1 acquired.")
            time.sleep(0.1)
            if lock2.acquire():
                print(self.name,"lock2 also acquired, lock1 was acuqired too")
                lock2.release()
            lock1.release()

class MyThread2(Thread):
    def run(self):
        if lock2.acquire():
            print(self.name, "lock2 acquired.")
            time.sleep(0.1)
            if lock1.acquire():
                print(self.name,"lock1 also acquired, lock2 was acuqired too")
                lock1.release()
            lock2.release()


if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread2()

    t1.start()
    t2.start()
    