from ast import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nu=set(nums1)
        nu2=set(nums2)
        return [nu-nu2,nu2-nu]
       