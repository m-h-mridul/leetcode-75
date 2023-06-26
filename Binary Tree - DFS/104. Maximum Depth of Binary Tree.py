class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:    
        if not root:
            return 0
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)
        output=max(left,right)
        output=output+1         
        return output