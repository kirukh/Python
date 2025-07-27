# Queue
import queue
import threading
import time

q = queue.Queue()

# Producer: fügt etwas in die Queue ein


def producer():
    for i in range(5):
        print(f"Produzent legt {i} in die Queue")
        q.put(i)
        time.sleep(1)

# Consumer: holt etwas aus der Queue


def consumer():
    while True:
        item = q.get()
        print(f"Konsument holt {item} aus der Queue")
        q.task_done()  # wichtig für .join()
        time.sleep(2)


# Threads starten
threading.Thread(target=producer).start()
threading.Thread(target=consumer, daemon=True).start()

q.join()  # wartet, bis alle Elemente verarbeitet wurden
print("Alle Aufgaben erledigt.")


# Semaphore
sema = threading.Semaphore(2)  # max. 2 Threads gleichzeitig


def arbeiter(name):
    print(f"{name} will rein...")
    with sema:
        print(f"{name} ist drin.")
        time.sleep(2)
    print(f"{name} ist raus.")


threads = [threading.Thread(target=arbeiter, args=(
    f"Thread-{i}",)) for i in range(4)]

for t in threads:
    t.start()


# Mutex
lock = threading.Lock()
counter = 0


def arbeite():
    global counter
    with lock:  # nur ein Thread darf hier rein
        for _ in range(100000):
            counter += 1


t1 = threading.Thread(target=arbeite)
t2 = threading.Thread(target=arbeite)

t1.start()
t2.start()
t1.join()
t2.join()

print("Counter:", counter)
