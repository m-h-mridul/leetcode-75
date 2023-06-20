class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        ans=""
        count=0
        for i in word1:
            if count<len(word2):
                ans+=i+word2[count]
                count+=1
            else:
                ans+=i
        ans+=word2[count:]
        return ans