import threading
import time

def listen_work(name):
    i=5
    while i>0:
        time.sleep(1)
        print(name,"正在处理文件")
        i-=1


def download_work(name):
    i=3
    while i>0:
        time.sleep(2)
        print(name,"正在下载文件")
        i-=1


if __name__ == '__main__':
    p1 = threading.Thread(target=listen_work,args=("多线程应用",))
    p2 = threading.Thread(target=download_work,args=("多线程应用",))
    p1.start()
    p2.start()