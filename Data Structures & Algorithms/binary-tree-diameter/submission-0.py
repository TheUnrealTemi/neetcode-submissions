# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.largest_dia = 0
        
        def height(node):
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)
            dia = left + right
            self.largest_dia = max(self.largest_dia, dia)

            return 1+ max(left, right)

        height(root)
        return self.largest_dia