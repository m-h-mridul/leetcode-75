

from typing import List


def nearestExit(maze: List[List[str]], entrance: List[int]) -> int:
    if (entrance[0] == 0 and entrance[1] == 0):
        return -1
    ansCheak = [(entrance[0], entrance[1])]
    m = len(maze)
    n = len(maze[0])
    i_entrence, j_entrance = entrance[0], entrance[1]
    count = 1000
    travellerCheak = set()
    travellerCheak.add(ansCheak[-1])

    while ansCheak:
        print(ansCheak)
        dummyCheak = []
        while ansCheak:
            temp = ansCheak.pop()
            i, j = temp[0], temp[1]

            if (i == 0 or i == m-1 or j == 0 or j == n-1) and (i != i_entrence or j != j_entrance):
                temp_2 = abs(i-i_entrence)+abs(j-j_entrance)
                if temp_2 > 0 and temp_2 < count:
                    count = temp_2
                continue

            if i+1 < m and maze[i+1][j] == '.' and (i+1, j) not in travellerCheak:
                dummyCheak.append((i+1, j))
                travellerCheak.add((i+1, j))
            if i-1 >= 0 and maze[i-1][j] == "." and (i-1, j) not in travellerCheak:
                dummyCheak.append((i-1, j))
                travellerCheak.add((i-1, j))
            if j-1 >= 0 and maze[i][j-1] == "." and (i, j-1) not in travellerCheak:
                dummyCheak.append((i, j-1))
                travellerCheak.add((i, j-1))
            if j+1 < n and maze[i][j+1] == "." and (i+1, j+1) not in travellerCheak:
                dummyCheak.append((i, j+1))
                travellerCheak.add((i, j+1))

        ansCheak.extend(dummyCheak)

    return count


ans = nearestExit(
    [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0])
print(ans)


def numMatchingSubseq(self, s: str, words: List[str]) -> int:
    tempF = collections.Counter(s)
    count = 0
    for i in words:
        temp = collections.Counter(i)
        if temp <= tempF:
            count += 1

    return count


