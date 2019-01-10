import threading
from queue import Queue
def thread_job(t,q):
    for i in range(len(t)):
        t[i] = t[i]**2
    q.put(t)
def main():

    data=[[1,2,3],[4,5,6],[7,8,9]]
    q=Queue()
    threads=[]
    for i in range(3):
        t1 = threading.Thread(target=thread_job,args=(data[i],q))
        t1.start()
        threads.append(t1)
    for thread in threads:
        thread.join()
    results = []
    for _ in range(3):
        results.append(q.get())
    print(results)
if __name__ == '__main__':
    main()
