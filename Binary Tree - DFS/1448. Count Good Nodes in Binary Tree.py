class Solution:
    def cal(self,root,preval):
        if not root:
            return 0
        
        if root.val>=preval:
            ans=1
        else:
            ans=0
        preval=max(preval,root.val)

        ans+=self.cal(root.left,preval)
        ans+=self.cal(root.right,preval)
        return ans
        
    def goodNodes(self, root: TreeNode) -> int:
        return self.cal(root,root.val)