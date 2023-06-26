class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans=[]
        if len(asteroids)<0:
            return asteroids
        else:
            i=0
            while i<len(asteroids):
                if asteroids[i]<0 and len(ans)>0 and ans[-1]>0:
                    if ans[-1]<abs(asteroids[i]):
                        ans.pop()
                    elif ans[-1]==abs(asteroids[i]):
                        ans.pop()
                        i+=1
                    else:
                        i+=1

                else:
                    ans.append(asteroids[i])
                    i+=1
        return ans