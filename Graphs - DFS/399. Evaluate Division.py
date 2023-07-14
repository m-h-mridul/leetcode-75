from ast import List
import collections
from multiprocessing.dummy.connection import Listener
from multiprocessing.managers import ListProxy
from xmlrpc.server import list_public_methods
class Solution:
    def calcEquation(self, equations: Listener[list_public_methods[str]], values: ListProxy[float], queries: List[List[str]]) -> List[float]:
        graph=collections.defaultdict(dict)
        for (i,j),val in zip(equations,values):
            graph[i][j]=val
            graph[j][i]=1.0/val
        print(graph)
        def dfs(x,y,visited):
            if x not in graph or y not in graph:
                return -1.0
            if y in graph[x]:
                return graph[x][y]

            for i in graph[x]:
                if i not in visited:
                    visited.add(i)
                    temp=dfs(i,y,visited)
                    if temp==-1:
                        continue
                    else:
                        return graph[x][i]*temp
            return -1

        res=[]
        for i in queries:
            res.append(dfs(i[0],i[1],set()))
        return res

