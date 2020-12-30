import threading


# Deadlocked -  when you try to lock a locked thread,
# you end up deadlocking the program
# lock = threading.Lock()
# lock.acquire()
# lock.acquire()

# To prevent deadlock you can use RLock (Re-entrant lock)
# this allows to make multiple calls to .acquire without
# deadlocking the program
rlock = threading.RLock()
rlock.acquire()
rlock.acquire()
print(rlock)
rlock.release()
print(rlock)
print(threading.current_thread())