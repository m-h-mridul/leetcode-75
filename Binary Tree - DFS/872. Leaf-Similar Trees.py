class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.cal(root1,[])==self.cal(root2,[])
       
    def cal(self,root,ans):
        if not root:
            return
        if not root.left and not root.right:
            ans.append(root.val)
        self.cal(root.left,ans)
        self.cal(root.right,ans)
        return ans
        