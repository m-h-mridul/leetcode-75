class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        currStr = ''
        currNum = 0
        for c in s:
            if c.isdigit():
                currNum=10*currNum+int(c)
            else:
                if c=="[":
                    stack.append((currStr,currNum))
                    currStr=""
                    currNum=0
                elif c=="]":
                    preStr,num=stack.pop()
                    currStr=preStr+num*currStr
                else:
                    currStr+=c
        return currStr
