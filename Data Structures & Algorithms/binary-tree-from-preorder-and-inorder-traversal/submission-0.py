# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Step 1: Map values to indices for O(1) root lookups in inorder array
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Track our current position in the preorder array
        self.pre_idx = 0
        
        def helper(in_start, in_end):
            # Base case: if there are no elements left in this subtree boundary
            if in_start > in_end:
                return None
            
            # Step 2: Grab the root value using our preorder tracker
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            
            # Step 3: Find where this root splits the inorder array
            pivot = inorder_map[root_val]
            
            # Step 4: Recursively build the left and right subtrees
            # Crucial: Build LEFT first because preorder is naturally ordered Root -> Left -> Right
            root.left = helper(in_start, pivot - 1)
            root.right = helper(pivot + 1, in_end)
            
            return root
            
        return helper(0, len(inorder) - 1)