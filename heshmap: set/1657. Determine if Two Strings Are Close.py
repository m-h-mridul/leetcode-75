import collections
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        ans=[]
        ans2=[]
        temp=collections.Counter(word1)
        temp2=collections.Counter(word2)
        for i in temp:
            if i in temp2:
                ans.append(temp[i])
            else: 
                return False
        for i in temp2:
            if i in temp2:
                ans2.append(temp2[i])
            else:
                return False
        print(ans,ans2)
        ans.sort()
        ans2.sort()
        return ans==ans2

