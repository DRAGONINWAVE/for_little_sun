import threading, time
from random import randint

class Producer(threading.Thread):
    def run(self):
        global StoreList
        while True:
            val = randint(0, 100)
            print('生产者', self.name, ':Append'+str(val),StoreList)
            if lock_con.acquire():
                StoreList.append(val)
                lock_con.notify()
                lock_con.release()
            time.sleep(3)

class Consumer(threading.Thread):
    def run(self):
        global StoreList
        while True:
            lock_con.acquire()
            if len(StoreList) == 0:
                lock_con.wait()
            print('消费者', self.name, ":Delete" + str(StoreList[0]), StoreList)
            del StoreList[0]
            lock_con.release()
            time.sleep(0.25)


if __name__ == "__main__":
    StoreList = []
    lock_con = threading.Condition()
    threads = []
    for i in range(5):
        threads.append(Producer())
    threads.append(Consumer())
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('---- end ----')