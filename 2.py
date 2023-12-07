
import os
import subprocess
import tempfile
import time
import threading
import random


def minimo(vec):
    min = vec[0]
    for i in vec:
        if i < min:
            min = i
    print("El numero minimo es " + str(min))
def mayor(vec):
    max = vec[0]
    for i in vec:
        if i > max:
            max = i
    print("El numero maximo es " + str(max))
def media(vec):
    media = 0
    for i in vec:
        media += i 
    media = media / len(vec)
    print("La media es " + str(media))
vector = []    
for i in range(100):
    vector.append(i)
t1 = threading.Thread(target=minimo, args = (vector,))
t2 = threading.Thread(target=mayor, args = (vector,))
t3 = threading.Thread(target=media, args=(vector,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

