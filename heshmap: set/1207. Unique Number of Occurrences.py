from ast import List
import collections 
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        temp=collections.Counter(arr)
        occurrences=set()
        print(temp)
        for i in temp.values():
            print(i)
            if i in occurrences:
                return False
            occurrences.add(i)
            
        return True