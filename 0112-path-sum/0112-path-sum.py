# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.fl=False
    def solve(self,root,targetSum,temp):
        if root==None:
            return

        temp+=root.val
        if  root.left is None and root.right is None and temp==targetSum:
            self.fl=True
        self.solve(root.left,targetSum,temp)
        self.solve(root.right,targetSum,temp)
        temp-=root.val
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        temp=0
        self.solve(root,targetSum,temp)
        return self.fl