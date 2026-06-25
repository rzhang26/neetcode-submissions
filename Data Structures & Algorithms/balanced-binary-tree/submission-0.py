# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkHeight(node):
            if not node:
                return 0

            left_height = checkHeight(node.left)
            if left_height == -1:
                return -1

            right_height = checkHeight(node.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return 1 + max(checkHeight(node.left), checkHeight(node.right))
        
        return checkHeight(root) != -1