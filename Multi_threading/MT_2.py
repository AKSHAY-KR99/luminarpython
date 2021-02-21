import threading
import time

def display():
    for i in range(1,10):
        time.sleep(2)
        print("child thread excecuting")
    print(threading.currentThread().getName())

t=threading.Thread(target=display)
t.start()
bigintime=time.time()
t.join()
print("beginig ",bigintime)
for i in range(1, 10):
    time.sleep(2)
    print("main thread excecuting")
print(threading.currentThread().getName())
endtime=time.time()
print("total time",endtime-bigintime)