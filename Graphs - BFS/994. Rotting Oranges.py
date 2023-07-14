
from ast import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        cheak=[]
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==2:
                    cheak.append((i,j))
        
        while cheak:
            add_cheak=[]
            while cheak:
                temp=cheak.pop(0)
                i,j=temp[0],temp[1]

                if  i-1>=0 and grid[i-1][j]==1:
                    grid[i-1][j]=2
                    add_cheak.append((i-1,j))

                if j-1>=0 and grid[i][j-1]==1:
                    grid[i][j-1]=2
                    add_cheak.append((i,j-1))

                if j+1 <len(grid[i]) and grid[i][j+1]==1:
                    grid[i][j+1]=2
                    add_cheak.append((i,j+1))

                if i+1<len(grid) and grid[i+1][j]==1:
                    grid[i+1][j]=2
                    add_cheak.append((i+1,j))

            

            if add_cheak:
                count+=1
                cheak.extend(add_cheak)
            

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    return -1
                
        return count

