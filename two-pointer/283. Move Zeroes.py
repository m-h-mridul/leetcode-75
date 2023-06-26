class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        ll=len(nums)
        co=0
        i=0
        while i<ll-co:
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
                co+=1
               
                continue
            i+=1
               