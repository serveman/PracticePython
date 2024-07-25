import threading, time

var = 0

def func():
    time.sleep(0.3)
    print('Current thread: ', threading.current_thread().getName())

for _ in range(10):
    threading.Thread(target=func).start()

print(threading.enumerate())
