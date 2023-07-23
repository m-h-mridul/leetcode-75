from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        def cal(temp,temp_array,target):

            
            if len(temp_array)==k:
                if target==0:
                    ans.append(temp_array)
                return


            for i in range(1+temp,10):
                if i<=target:
                    cal(i,temp_array+[i],target-i)

                    
        cal(0,[],n)
        return ans
      