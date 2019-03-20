import BufferHeader
import numpy as np
class HashQueue(object):
    def __init__(self,size):
        self.size=size
        self.hashQ=np.empty(self.size,dtype=object)
        for i in range(self.size):
            self.hashQ[i]=None
            

    def findBlockInHashQ(self, blockNumber ):
        queue=possibleBlock=self.hashQ[blockNumber%self.size] #possible queue
        while(queue!=None):
            if(possibleBlock.getBlockNumber()==blockNumber):
                return possibleBlock #block is found

            possibleBlock=possibleBlock.getNextHashQ()
            
            if(possibleBlock==queue):
                break

        return None

    def isPresentinHashQ(self,blockNumber):
        if(self.findBlockInHashQ(blockNumber)!=None):
            return True
        return False

    def addBlockToHashQ(self,block):
        queueStart=self.hashQ[block.getBlockNumber() %self.size] #queue to which the block has to be added 
        
        if (queueStart==None):#if queue is empty
            self.hashQ[block.getBlockNumber() %self.size]=block
            block.addNextHashQ(block)
            block.addPrevHashQ(block)
            return 1 ##success
        queueEnd=queueStart.getPrevHashQ()

        queueEnd.addNextHashQ(block)
        block.addPrevHashQ(queueEnd)

        block.addNextHashQ(queueStart)
        queueStart.addPrevHashQ(block)
               
        return 1

    def removeFromHashQ(self,block):
        if(block.getNextHashQ()==block):#only one element in hashQ
            self.hashQ[block.getBlockNumber()%self.size]=None
            return 1
        
        block.getPrevHashQ().addNextHashQ(block.getNextHashQ())
        block.getNextHashQ().addPrevHashQ(block.getPrevHashQ())

    def printHashQ(self):
        for i in range(self.size):
            block=self.hashQ[i]
            while(block!=None):
                print("<-",block.getBlockNumber(),"->" )
                block=block.getNextHashQ()
                if(block==self.hashQ[i]):
                    break
            
            print("\n")
            


if __name__=="__main__":
    # hQ=HashQueue(4)
    # for i in range(20):
    #     block=BufferHeader.BufferHeader(i)
    #     hQ.addBlockToHashQ(block)
    #     hQ.printHashQ()
    #     print("end")
    


    

        
    