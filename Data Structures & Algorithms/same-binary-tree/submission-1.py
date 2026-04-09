# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p:
            if q:
                if p.val == q.val:
                    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                if not q and p.val == None:
                    return True
                else:
                    return False
        else:
            if q:
                return False
            else:
                if not p and not q:
                    return True
                else:
                    return False
        return False

            