class Solution:
    def guessNumber(self, n: int) -> int:
        start=1
        while True:
            middle=(start+n)//2
            if guess(middle)==0:
                return middle
            elif guess(middle)==1:
                start=middle+1
            else:
                n=middle
        