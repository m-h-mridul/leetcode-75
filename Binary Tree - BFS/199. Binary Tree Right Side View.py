class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root,ans,level):
            if not root:
                return
            if root and level==len(ans):
                ans.append(root.val)
            dfs(root.right,ans,level+1)
            dfs(root.left,ans,level+1)
            return ans
        return dfs(root,[],0)