class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        compare=root.val
        ans=1
        queueRoot= collections.deque([root])
        level=1
        print(queueRoot)

        while queueRoot:
            lenght=len(queueRoot)
            i=0
            summ=0
            while i<lenght:
                temp=queueRoot.popleft()
                summ+=temp.val
                if temp.left:
                    queueRoot.append(temp.left)
                if temp.right:
                    queueRoot.append(temp.right)
                i+=1
            if compare<summ:
                ans=level
                compare=summ
            level+=1
                
        return ans

