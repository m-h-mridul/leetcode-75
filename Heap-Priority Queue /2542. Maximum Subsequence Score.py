from ast import List
import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res=0
        head=[]
        total=0
        for i, n in sorted(zip(nums2,nums1),reverse=True):
            print(i,n,head,total)
            if len(head)==k:
                total-=heapq.heappop(head)
                
            total+=n
            heapq.heappush(head,n)
            if len(head)==k:
                res=max(res,i*total)
        return res
