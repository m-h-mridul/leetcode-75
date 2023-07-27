class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 1e9 + 7
        ans = [0] * 1001
        ans[0]=0
        ans[1]=1
        ans[3]=5
        ans[2]=2
        if n<=3:
            return ans[n]
        for i in range(4,n+1):
            ans[i]=2*ans[i-1]+ans[i-3]
            ans[i]%=MOD
        return int(ans[n])