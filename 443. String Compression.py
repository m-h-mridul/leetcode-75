class Solution:
    def compress(self, chars: List[str]) -> int:
        count=0
        ans=chars.copy()
        chars.clear()
        for i in range(0,len(ans)):
            count+=1
            if i==len(ans)-1 or ans[i]!=ans[i+1]:
                if count>1:
                    chars.append(ans[i])
                    a=str(count)
                    for j in a:
                        chars.append(j)
                    
                else:
                     chars.append(ans[i])
                count=0
        
        return len(chars)
                    