# Threads
import multiprocessing
import threading

counter = 0
lock = threading.Lock()


def worker():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1


threads = [threading.Thread(target=worker) for _ in range(2)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Thread Counter:", counter)


# Prozesse


def worker(shared_counter):
    for _ in range(100000):
        with shared_counter.get_lock():
            shared_counter.value += 1


if __name__ == "__main__":
    counter = multiprocessing.Value('i', 0)
    p1 = multiprocessing.Process(target=worker, args=(counter,))
    p2 = multiprocessing.Process(target=worker, args=(counter,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Process Counter:", counter.value)

# In multiprocessing brauchst du Value, Array oder Manager, um Daten zu teilen.
