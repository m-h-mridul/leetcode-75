class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i=0
        c=0
        while c<len(s) and i<len(t):
            if s[c]==t[i]:
                c+=1
            i+=1
        if c== len(s):
            return True
        return False