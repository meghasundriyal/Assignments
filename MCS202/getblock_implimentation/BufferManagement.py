import multiprocessing
import AsynchronousWrite
import time
import os
def getBlock(blockNumber,lock,hashQ,freeList):
    bufferFound=False
    while (not bufferFound):

        lock.acquire()#lock
        if (hashQ.isPresentInHashQ(blockNumber)):

            buffer=hashQ.findBlockInHashQ(blockNumber)
            if(buffer.isLocked()):



                #for revealing the scenario under which process is going to sleep
                print("process: ",os.getpid()," is going to sleep as buffer ",buffer.getBlockNumber()," is present in hashQ and is busy")
                # print("from here: ") , 
                # freeList.printFreeList()
                
                lock.release()
                time.sleep(4)
                continue
            buffer.setLockedBit()
            freeList.removeFromFreeList(buffer)

            #for revealing the scenario under which process is going to sleep
            print("process: ",os.getpid(),"  will get buffer  ",buffer.getBlockNumber()," from hashQ")

            lock.release()
            return buffer
        else:
            if (freeList.isEmpty()):

                #for revealing the scenario under which process is going to sleep
                print("process: ",os.getpid()," is going to sleep as freeList is empty")

                lock.release()
                time.sleep(4)
                continue
            buffer=freeList.removeAnyFromFreeList()
            if(buffer.isDelayedWrite()):

                #for revealing the scenario under which process is going to sleep
                print("process: ",os.getpid()," came across block number: ",buffer.getBlockNumber(), "marked as delayed write so is executing asynchronous write")

                
                lock.release()
                AsynchronousWrite.asynchronousWrite(lock,buffer)
                continue
            hashQ.removeFromHashQ(buffer)

            print("process: ",os.getpid()," is will replace buffer  ",buffer.getBlockNumber(),"  from freeList with buffer ",blockNumber)

            buffer.setBlockNumber(blockNumber)
            buffer.setLockedBit()
            hashQ.addBlockToHashQ(buffer)
            buffer.clearValidBit()#making it invalid

            #for revealing the scenario under which process is returning
            # print("process: ",os.getpid()," is will get buffer  ",buffer.getBlockNumber(),"  from freeList")

            lock.release()
            return buffer

                

            

