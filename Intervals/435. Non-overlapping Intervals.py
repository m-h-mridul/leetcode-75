from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans=0
        intervals.sort()
        prevalue=intervals[0][1]
        for start,end in intervals[1:]:
            if start>=prevalue:
                prevalue=end
            else:
                ans+=1
                prevalue=min(prevalue,end)
        return ans