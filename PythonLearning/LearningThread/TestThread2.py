import threading
import  time
def thread1_job():
    print('T1 run')
    for i in range(10):
        time.sleep(0.1)
    print('t1 finish')
def thread2_job():
    print('T2 run')
    print('t2 finish')
def main():
    print("main run")
    threading1 = threading.Thread(target=thread1_job,name='T1')
    threading1.start()
    threading2 = threading.Thread(target=thread2_job, name='T2')
    threading2.start()
    threading1.join()
    print(('main finish'))
if __name__ == '__main__':
    main()
