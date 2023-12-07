from multiprocessing.pool import ThreadPool
import os
import subprocess
import tempfile
import time
import threading
import random


def saludar(name):
    for i in range(random.randint(5,15)):
        time.sleep(random.randint(1, 3)/10)
        print("I am " + str(name))
    

pool = ThreadPool(processes=10)
pool.map(saludar,range(10))




