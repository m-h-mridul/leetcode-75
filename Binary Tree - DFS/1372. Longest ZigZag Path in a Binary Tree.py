class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans=0
        def cal (root,left,right):
            if not root:
                return 
            nonlocal ans
            ans=max(ans,left,right)
            cal(root.left,right+1,0)
            cal(root.right,0,left+1)
     
        cal(root,0,0)
        return ans
