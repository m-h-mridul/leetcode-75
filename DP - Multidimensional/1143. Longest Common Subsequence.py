class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        lcs=[[0 for j in range(0,len(text2)+1)] for i in range(0,len(text1)+1)]
        print(lcs)
        text1='0'+text1
        text2='0'+text2
        for i in range(1,len(text1)):
            for j in range(1,len(text2)):
                if text1[i]==text2[j]:
                    lcs[i][j]=1+lcs[i-1][j-1]
                else:
                    lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1])
           
        return lcs[-1][-1] 