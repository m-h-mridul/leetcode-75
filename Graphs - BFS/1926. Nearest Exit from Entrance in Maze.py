from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ansCheak = [(entrance[0], entrance[1])]
        m = len(maze)
        n = len(maze[0])
        i_entrence, j_entrance = entrance[0], entrance[1]
        count = 1000
        ans=-1
        travellerCheak=set()
        travellerCheak.add(ansCheak[-1])

        while ansCheak:
            dummyCheak = []
            ans+=1
            while ansCheak:
                temp = ansCheak.pop()
                i, j = temp[0], temp[1]

                if (i == 0 or i == m-1 or j == 0 or j == n-1) and (i != i_entrence or j != j_entrance):
                    return ans

                if i+1 < m and maze[i+1][j] == '.' and (i+1, j) not in  travellerCheak:
                    dummyCheak.append((i+1, j))
                    travellerCheak.add((i+1, j))
                if i-1 >= 0 and maze[i-1][j] == "." and (i-1, j) not in  travellerCheak:
                    dummyCheak.append((i-1, j))
                    travellerCheak.add((i-1, j))
                if j-1 >= 0 and maze[i][j-1] == "." and (i, j-1) not in  travellerCheak:
                    dummyCheak.append((i, j-1))
                    travellerCheak.add((i, j-1))
                if j+1 < n and maze[i][j+1] == "." and (i, j+1) not in  travellerCheak:
                    dummyCheak.append((i, j+1))
                    travellerCheak.add((i, j+1))

            ansCheak.extend(dummyCheak)
        return -1
