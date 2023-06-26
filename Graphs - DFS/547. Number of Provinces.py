class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(n):
                n2=len(isConnected)
                for j in range(0,n2):
                    if visited[j]==False and isConnected[n][j]==1:
                        visited[j]=True
                        dfs(j)

                        
        n=len(isConnected)
        grope=0
        visited= [False] * n
        for i in range(0,n):
            if visited[i]==False:
                dfs(i)
                grope+=1
                
        return grope