class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        def cal(root,pre):
            ans=0
            if not root:
                return ans
            if root.val==pre:
                ans+=1
            ans+=cal(root.left,pre-root.val)
            ans+=cal(root.right,pre-root.val)
            return ans
        return cal(root,targetSum)+self.pathSum(root.left,targetSum)+self.pathSum(root.right,targetSum)