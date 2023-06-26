class Solution:
    def removeStars(self, s: str) -> str:
        ans=''
        for i in range(len(s)):
            if s[i]=='*':
                ans=ans[:-1]
            else:
                ans+=s[i]
        print(ans)
        return ans
