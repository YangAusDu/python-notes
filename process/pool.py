from multiprocessing import Pool
import time
from random import random
import os


def task(task_name):
    print("[+]Task starts!!", task_name, "process: ", os.getpid())
    start = time.time()
    time.sleep(random()*2)
    end = time.time()
    print("\n{} completed!! takes: {} seconds".format(task_name, end- start))

def callback_func(task_name):
    container.append(task_name)
    


if __name__ == "__main__":
    pool = Pool(5)
    container = []
    tasks = ["Listening music", "Singing a song", "Eatting lunch", "Laudry", "Play games", "Jogging", "babysitting", "workout"]
    for each_task in tasks:
        pool.apply_async(func= task, args=(each_task,),callback= callback_func(each_task))  #pool.appy()


    pool.close()
    pool.join()
    print(container)

    print("over")