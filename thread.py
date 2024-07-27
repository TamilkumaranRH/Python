""" import threading

import time

print("Time when code execution begin is: ", end ="")

print(time.ctime())

time.sleep(5)

print("Time when code execution end is : ", end ="")

print(time.ctime()) """

import threading
import time
def number():
    for i in range(1,5):
        print(i)
        time.sleep(3)

def alphabet():
    for char in ['A', 'B', 'C', 'D', 'E']:
        print(char)
        time.sleep(1)
thread1 = threading.Thread(target=number)

thread2 = threading.Thread(target=alphabet)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("threading is finish")        
