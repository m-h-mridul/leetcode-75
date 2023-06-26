class RecentCounter:
    def __init__(self):
        self.ans=[]
        
    def ping(self, t: int) -> int:
        self.ans.append(t)
        while self.ans[0]<t-3000:
            self.ans.pop(0)
        return len(self.ans)