#!/usr/bin/python

import config
from libs.PasteSiteParser import PasteSiteParser
from libs.Services import GetServices
import config
import libs.Reusables as Reusables
import sys
import queue
import threading
import time
import random

class Threader (threading.Thread):
    def __init__(self, threadID, name, q):
        """
        :param threadID:
        :param name:
        :param q:
        """
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        """
        run()

        :return:

        Run the application with threading

        """
        Reusables.write_log("[{0}] Starting {1}".format(config.APP, self.name))
        process(self.name, self.q)
        Reusables.write_log("[{0}] Exiting {1}".format(config.APP, self.name))

def process(threadName, q):
    """
    process(threadName, q)

    :param threadName:
    :param q:
    :return:

    Process the queued item with threadName

    """
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            for [service, pages, viewall, viewpaste, tag, tag_end] in [data]:
                Reusables.write_log("[{0}] Parsing service {1}...".format(config.APP, service))
                sw = PasteSiteParser(service, pages, viewall, viewpaste, tag, tag_end)
                sw.begin()
        else:
            queueLock.release()
            pause = random.randint(5, 10)
            Reusables.write_log("[{0}] Work queue is empty, sleeping for {1} seconds....".format(config.APP, pause))
            time.sleep(pause)

"""

Beginning of the application

"""

# Create a list of threads
threadList = []
tCount = 1
while tCount <= config.THREAD_COUNT:
    threadList.append("Thread-{0}".format(tCount))
    tCount += 1

# Set exitFlag, services, and workQueue
exitFlag = 0
services = GetServices()
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
   thread = Threader(threadID, tName, workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1

# Fill the queue
queueLock.acquire()
for service in services:
   workQueue.put(service)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
    pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
    t.join()

Reusables.write_log("[{0}] Exiting Main Thread".format(config.APP))
