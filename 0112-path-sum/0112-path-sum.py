# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.fl=False
    def solve(self,root,targetSum):
        if root==None:
            return
        targetSum-=root.val
        if  root.left is None and root.right is None and targetSum==0:
            self.fl=True
        self.solve(root.left,targetSum)
        self.solve(root.right,targetSum)


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        self.solve(root,targetSum)
        return self.fl