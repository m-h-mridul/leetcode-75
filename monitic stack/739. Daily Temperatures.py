from ast import ListComp
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: ListComp[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []
        pre=0
        for i in range(0, len(temperatures)):
            stack.append(i)
            if len(stack) >= 2:
                while temperatures[stack[pre]] < temperatures[stack[-1]]:
                    ans[stack[pre]] = stack[-1]-stack[pre]
                    stack.pop(pre)
                    pre-=1
                pre += 1
        return ans