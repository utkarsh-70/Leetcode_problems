"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        def po(root,li):
            if not root:
                return li
            for i in root.children:
                po(i,li)
                li.append(i.val)
            return li
        return po(root,[])+[root.val]