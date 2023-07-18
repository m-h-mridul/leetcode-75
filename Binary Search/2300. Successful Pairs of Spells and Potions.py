from ast import List


class Solution:

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def bi(potions,s,e,i):
            while s<e:
                m=(s+e)//2
                if potions[m]*i>=success and (m==0 or potions[m-1]*i<success):
                   
                    return m
                if potions[m]*i>=success:
                    e=m
                else:
                    s=m+1
            return -1

        ans=[]
        potions.sort()
        for i in spells:
            s=0
            e=len(potions)
            tempC=bi(potions,s,e,i)
            
            if tempC==-1:
                tempC=0
            else:
                tempC=e-tempC
           
            
            ans.append(tempC)
        return ans


