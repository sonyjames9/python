import threading
import time

thread_list = []


def count(n):
  for i in range(1, n+1):
    print(f"count 1 : {i}")
    time.sleep(0.01)


def count2(n):
  for i in range(1, n+1):
    print(f"count 2 : {i}")
    time.sleep(0.02)
    thread_list.append(i)


def count3(n):
  for i in range(1, n+1):
    print(f"count 3 : {i}")
    time.sleep(0.02)
    thread_list.append(i)


# for _ in range(2):
x = threading.Thread(target=count, args=(10,))
print(f"Thread Active count 1 : {threading.activeCount()}")
x.start()

y = threading.Thread(target=count2, args=(10,))
print(f"Thread Active count 2 : {threading.activeCount()}")
y.start()

y.join()
z = threading.Thread(target=count3, args=(10,))
print(f"Thread Active count 3 : {threading.activeCount()}")
z.start()

print("Done")

z.join()

print(f" Thread list : {thread_list}")
