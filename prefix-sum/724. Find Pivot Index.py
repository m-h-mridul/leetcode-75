from ast import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summ=sum(nums)
        leftsum=0
        for i,num in enumerate(nums):
            if leftsum == summ-num-leftsum:
                return i
            leftsum+=num
        return -1