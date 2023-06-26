class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        qr=[]
        qd=[]
        length=len(senate)
        for i in range(length):
            if "R" ==senate[i]:
                qr.append(i)
            else:
                qd.append(i)
        
        while qr and qd:
            temp=qr.pop(0)
            temp2=qd.pop(0)
            if temp<temp2:
                qr.append(length+temp)
            else:
                qd.append(length+temp2)
        if qr:
            return "Radiant"
        else:
            return "Dire"
