class StockSpanner:

    def __init__(self):
        self.li=[]
        self.temp={0:0}
        
    def next(self, price: int) -> int:
        le=len(self.li)-1
        ans=0
        while le>=0:
            if self.li[le]<=price:
                ans+=self.temp.get(self.li[le],0)
                self.li.pop(le)
            else:
                break
            le-=1
        self.li.append(price)
        self.temp[price]=ans+1
        return ans+1  

        


