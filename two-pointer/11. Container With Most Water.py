class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        l=len(height)-1
        result=0
        while(i<l):  
            max_ans=(l-i)*min(height[l],height[i])
            if max_ans>result:
                result=max_ans
            if height[i]<height[l]:               
                i+=1
            else:
                l-=1
        return result 