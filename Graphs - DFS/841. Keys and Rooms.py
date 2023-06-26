class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        ans =[False]*n
        def dfs(room,i):
            if ans[i]:
                return    
            ans[i]=True
            for z in room[i]:
                dfs(room,z)

        dfs(rooms,0)           
        for c in ans:
            if c==False:
                return False
        return True
        