# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#DFS approach --> uses 1 + max(height left & right) to include current node 
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkHeight(node) -> int:
            if not node:
                return 0

            height_left = checkHeight(node.left)
            if height_left == -1:
                return -1
            
            height_right = checkHeight(node.right)
            if height_right == -1:
                return -1

            if abs(height_right - height_left) > 1:
                return -1

            return 1 + max(height_left, height_right)

        return checkHeight(root) != -1