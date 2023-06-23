class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        ans=0
        print(nums)
        while (i<j):
            if nums[i]+nums[j]==k:
                print(nums[i],nums[j])
                ans+=1
                i+=1
                j-=1
            elif k-nums[i]<nums[j]:
                j-=1
            elif k-nums[i]>nums[j]:
                i+=1
            else:
                i+=1
                j-=1
        return ans

            