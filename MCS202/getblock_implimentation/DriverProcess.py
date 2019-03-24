import random
import BufferHeader
import multiprocessing
from multiprocessing.managers import BaseManager
from multiprocessing import Process, Manager
import random
import time
import BufferDataStructure
import BufferHeader
import BufferManagement
import os
import myProcess




lengthOfHashQ=4
freeListSize=20
maxNoOfBlocks=30

#using shared memory objects using BaseManager from multiprocessing library
BaseManager.register('BufferDataStructure',BufferDataStructure.BufferDataStructure)
manager=BaseManager()
manager.start()

bufferDataSructure=manager.BufferDataStructure(freeListSize,lengthOfHashQ)
bufferDataSructure.mapFreeListIntoHashQ()

print("Initial State of hashQ")
bufferDataSructure.printHashQ()
print("Initial State of freeList")
bufferDataSructure.printFreeList()

lock=multiprocessing.Lock()
p1=multiprocessing.Process(target=myProcess.process,args=(bufferDataSructure,lock,maxNoOfBlocks,))
p2=multiprocessing.Process(target=myProcess.process,args=(bufferDataSructure,lock,maxNoOfBlocks,))
p3=multiprocessing.Process(target=myProcess.process,args=(bufferDataSructure,lock,maxNoOfBlocks,))
p1.start()
p2.start()
p3.start()
p1.join()
p2.join()
p3.join()
print("end")








