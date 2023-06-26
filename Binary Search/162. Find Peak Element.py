class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        began=0
        end=len(nums)-1
        while began<end:
            middle=(began+end)//2
            if nums[middle]<nums[middle+1]:
                began=middle+1
            else:
                end=middle
        return end