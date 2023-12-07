
import os
import subprocess
import tempfile
import time
import threading
import random


def sumar(name):
    progreso = 0
    for i in range(100):
        progreso += random.randint(1,1000)
    print("El hilo " + str(name) + " ha sacado el numero " + str(progreso))

t1 = threading.Thread(target=sumar, args = [1,])
t2 = threading.Thread(target=sumar, args = [2,])
t3 = threading.Thread(target=sumar, args =[ 3,])
t4 = threading.Thread(target=sumar, args = [4,])
t5 = threading.Thread(target=sumar, args = [5,])
t6 = threading.Thread(target=sumar, args = [6,])
t7 = threading.Thread(target=sumar, args = [7,])
t8 = threading.Thread(target=sumar, args = [8,])
t9 = threading.Thread(target=sumar, args = [9,])
t10 = threading.Thread(target=sumar, args =[ 10,])
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()