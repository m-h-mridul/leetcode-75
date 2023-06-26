from ast import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=[0]
        for i in gain:
            ans.append(i+ans[-1])
        ans.sort()
        return ans[-1]