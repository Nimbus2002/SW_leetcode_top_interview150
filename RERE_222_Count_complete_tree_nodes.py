# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 # 아무것도 없으면 0
        r = self.get_depth(root.left, True) + 1
        l = self.get_depth(root.right, False) +1
        if r == l:
            return (1<<r) -1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def get_depth(self, node, left):
        d = 0
        while node:
            node = node.left if left else node.right
            d +=1

        return d
        
