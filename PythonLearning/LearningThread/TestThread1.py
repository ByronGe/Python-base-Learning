import threading
def thread_job():
    print("this is an add thread job,number is %s"%threading.current_thread())

def main():



    added_thread = threading.Thread(target=thread_job)
    added_thread.start()
    print(threading.current_thread())
    print(threading.active_count())
    print(threading.enumerate())
if __name__ == '__main__':
    main()
