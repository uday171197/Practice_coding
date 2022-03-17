import threading

t = threading.current_thread().getName()

print('sample')

print(t) # It will return thread name in which the code is running `MainThread`

