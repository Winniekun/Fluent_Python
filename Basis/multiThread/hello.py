"""
@Time : 19-4-14 下午4:16
@Author : KongWiki
@File : hello.py
@Email : kongwiki@163.com
"""
from threading import Thread
from time import sleep


class CookBook(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.message = 'Hello Parallel Python CookBook!!! \n'

    def print_message(self):
        print(self.message)

    def run(self):
        print('Thread Starting\n')
        x = 0
        while(x < 10):
            self.print_message()
            sleep(2)
            x += 1
        print("Thread Ended \n")


# print("Process Started")
# helloPython = CookBook()
# helloPython.start()
# print("Process Ended")

def function(i):
    print("function called by thread %i\n" %i)
    return


threads = []
for i in range(5):
    t = Thread(target=function, args=(i,))
    threads.append(t)
    t.start()
    t.join()
