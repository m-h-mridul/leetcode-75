class Solution:
    def reverseVowels(self, s: str) -> str:
        stack=[]
        ans=""
        cheak=['a', 'e', 'i', 'o','u','A','E','I','O','U']
        for i in s:
            if i in cheak:
                stack.append(i)
        for i in range(len(s)):
            if s[i] in cheak:
                ans+=stack.pop()
            else:
                ans+=s[i]

        return ans
        