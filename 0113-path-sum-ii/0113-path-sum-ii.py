# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.out=[]
    def find(self,head,tempsum,arr,targetSum):
        if head==None:
            return
        
        tempsum+=head.val
        arr.append(head.val)
        self.find(head.left,tempsum,arr,targetSum)
        self.find(head.right,tempsum,arr,targetSum)
        if head.left==None and head.right==None and targetSum==tempsum:
            self.out.append(arr[:])
        tempsum-=head.val
        arr.pop(-1)


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        arr=[]
        self.find(root,0,arr,targetSum)
        return self.out