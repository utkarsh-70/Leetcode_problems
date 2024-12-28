# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        lvlmax=[-float('inf')]*(10**4)
        md=0
        def dfs(root,depth):
            nonlocal md
            if not root:
                return 
            lvlmax[depth]=max(lvlmax[depth],root.val)
            md=max(md,depth)
            dfs(root.left,depth+1)
            dfs(root.right,depth+1)
        dfs(root,0)
        return lvlmax[:md+1]
        
