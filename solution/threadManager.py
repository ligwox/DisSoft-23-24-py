import threading
import time

class ThreadManager:
    def __init__(self):
        self.threads = []

    def addBeastThread(self, beast):
        thread=threading.Thread(target=beast.start)
        self.threads.append(thread)
        
    def addBossThread(self, boss):
        thread=threading.Thread(target=boss.start)
        self.threads.append(thread)

    def start(self):
        for thread in self.threads:
            print("Starting thread:", thread)
            thread.start()

    def join(self):
        for thread in self.threads:
            thread.join()

    def stop(self):
        for thread in self.threads:
            thread.stop()  
