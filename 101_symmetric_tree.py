# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(n1, n2): 
            if not n1 and not n2:
                return True
                # 둘다 없으면 true
            if not n1 or not n2:
                return False # 둘중에 하나만 없으면 false (둘다 포함되는 것은 위에서 잡힘)
            return n1.val == n2.val and is_mirror(n1.left, n2.right) and is_mirror(n1.right, n2.left)

        return is_mirror(root.left, root.right)
        
