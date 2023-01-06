import threading
import time


def thread_fn():
  print("thread run")
  time.sleep(1)
  print("sleep")
  time.sleep(1)
  print("complete")


# x = threading.Thread(target=thread_fn, args=(4,))
x = threading.Thread(target=thread_fn)
x.start()

print(threading.activeCount())
time.sleep(1)
print("finally")
