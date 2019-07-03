from threading import Thread
import time

value = 5 

class MyThread(Thread):
    def run(self):
        time.sleep(5)
        value = None

def get_value(thethread):
    if thethread.is_alive() :
        return value
    else :
        return value

def main():
    thethread = MyThread()
    thethread.start()
    print(get_value(thethread)) #should print value = 5
    time.sleep(6) # waiting the thread to finish
    print(get_value(thethread)) #makeing sure the value deleted