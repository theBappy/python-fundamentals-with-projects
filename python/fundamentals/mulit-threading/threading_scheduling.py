import threading
import time

def schedule_event(name, start):
    now = time.time()
    elapsed = int(now - start)
    print("Elapsed: ", elapsed, "Name: ", name)

start = time.time()
print("Start: ", time.ctime(start))

# Schedule events using Timer
t1 = threading.Timer(3, schedule_event, args=('EVENT_1', start))
t2 = threading.Timer(2, schedule_event, args=('EVENT_2', start))

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()
print('End:', time.ctime(end))

