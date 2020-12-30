import threading

sem = threading.Semaphore(value=50)
print(sem._value)
sem.acquire()
sem.acquire()
sem.acquire()
sem.release()
print(sem._value)
