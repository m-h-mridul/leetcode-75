class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        ans=0
        dummyList=[]
        i=0
        l=len(flowerbed)
        while i<l:
            if flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and (i==l-1 or flowerbed[i+1]==0):
                flowerbed[i]=1
                ans+=1
                i+=1
            else:
                i+=1
       
        return ans>=n
