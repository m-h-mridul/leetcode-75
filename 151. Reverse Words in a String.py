class Solution:
    def reverseWords(self, s: str) -> str:
        ans=""
        s.split(" ")
        re=s.split()
        print(re)
        for i in range(len(re)-1,-1,-1):
            ans+=str(re[i])
            if i!=0:
                ans+=" "
        return ans