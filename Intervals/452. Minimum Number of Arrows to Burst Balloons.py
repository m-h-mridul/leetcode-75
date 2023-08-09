class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        v=points
        ans=0
        preEnd=-21474836489003
        for start,end in sorted(v, key=lambda x: x[1]):
            if preEnd<start:
                ans+=1
                preEnd=end
        return ans