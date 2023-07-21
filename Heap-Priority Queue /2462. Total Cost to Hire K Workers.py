import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ans=0
        j=len(costs)-1
        i=0
        minheapL=[]
        minheapR=[]
        while k:
            while len(minheapL)<candidates and i<=j:
                heapq.heappush(minheapL,costs[i])
                i+=1
            while len(minheapR)<candidates and i<=j:
                heapq.heappush(minheapR,costs[j])
                j-=1
            k-=1
            if not minheapR:
                ans+=heapq.heappop(minheapL)
            elif  not minheapL:
                ans+=heapq.heappop(minheapR)
            elif minheapL[0]<=minheapR[0]:
                ans+=heapq.heappop(minheapL)
            else:
                ans+=heapq.heappop(minheapR)
        return ans
    
        

