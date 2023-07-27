from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        ans,ans2=0,0
        for i in nums:
            temp=max(i+ans,ans2)
            ans=ans2
            ans2=temp
        return ans2
                
            
