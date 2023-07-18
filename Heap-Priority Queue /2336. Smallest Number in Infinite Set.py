import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.min=1
        self.smallestset=[]
        

    def popSmallest(self) -> int:
        print(self.min)
        if len(self.smallestset)>0:
            return heapq.heappop(self.smallestset)
        self.min+=1
        return self.min-1
        
        

    def addBack(self, num: int) -> None:
        if  num < self.min and  num not in self.smallestset:
            heapq.heappush(self.smallestset,num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)