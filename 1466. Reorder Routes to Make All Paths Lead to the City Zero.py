from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        # here make a dictionary for travelling the node
        for con in connections:
            a,b = con
            adj_list[a].append(b)
            adj_list[b].append(-a)
        # make a dummy node variavbe for cheak if node tavelling or not 
        self.visited=[0]*n
        # the cal function cheak if user visite the nood or not 
        #  if visite the continie cannot visite and also creat 
        # another funtion to visted and doing the nexrt aatsk

        def cal(start):
            count=0
            for i in adj_list[start]:
                if self.visited[abs(i)]==1:
                    continue
                if i >0:
                    count+=1
                self.visited[abs(i)]=1
                count+=cal(abs(i))
            return count
        return cal(0)