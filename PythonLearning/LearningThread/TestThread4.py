import threading
from queue import Queue

def jop1():
    global lock
    a=0
    lock.acquire()
    for i in range(10):
        a+=i
        print('a=',a)
    lock.release()
def jop2():
    b=0
    lock.acquire()
    for i in range(100):
        b+=i
        print('b=',b)
    lock.release()
if __name__ == '__main__':
    lock = threading.Lock()
    t1 = threading.Thread(target=jop1)
    t2 = threading.Thread(target=jop2)
    t1.start()
    t2.start()
    t2.join()
