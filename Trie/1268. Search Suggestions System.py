class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans=[]
        cheak=''
        products.sort()
        for i in range(0,len(searchWord)):
            temp=[]
            cheak+=searchWord[i]
            for j in products:
               
                if j[0:i+1]==searchWord[0:i+1]:
                    temp.append(j)
            ans.append(temp[0:3])
        return ans