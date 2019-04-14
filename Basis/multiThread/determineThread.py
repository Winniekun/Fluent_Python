"""
@Time : 19-4-14 下午5:09
@Author : KongWiki
@File : determineThread.py
@Email : kongwiki@163.com 
"""
import threading
import time


def first():
    print(threading.currentThread().getName() + str(' is Starting'))
    time.sleep(2)
    print(threading.currentThread().getName() + str(' is Exiting \n'))
    return


def second():
    print(threading.currentThread().getName() + str(' is Starting'))
    time.sleep(2)
    print(threading.currentThread().getName() + str(' is Exiting \n'))
    return


def third():
    print(threading.currentThread().getName() + str(' is Starting'))
    time.sleep(2)
    print(threading.currentThread().getName() + str(' is Exiting \n'))
    return


exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("starting " + self.name)
        printName(self.name, self.counter, 5)
        print('exiting ' + self.name)


def printName(threadName, delay, counter):
    while counter:
        if exitFlag:
            threading.exit()
        time.sleep(delay)
        print("%s: %s" %
              (threadName, time.ctime(time.time())))
        counter -= 1


if __name__ == '__main__':
    # t1 = threading.Thread(name='first', target=first)
    # t2 = threading.Thread(name='second', target=second)
    # t3 = threading.Thread(name='third', target=third)

    # t1.start()
    # t2.start()
    # t3.start()
    # t1.join()
    # t2.join()
    # t3.join()

    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("Exiting Main Tread")



