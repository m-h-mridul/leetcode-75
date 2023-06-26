class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        c=0
        preco=0
        for i in range (len(grid[0])):
            temp=[]
            for j in range (len(grid[0])):
                temp.append(grid[j][i])

            print(temp)
            if temp in grid:
                c+=grid.count(temp)
                preco=max(preco,c)
        return preco