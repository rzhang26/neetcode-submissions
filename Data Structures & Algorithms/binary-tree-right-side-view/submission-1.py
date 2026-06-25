# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = deque([root]) 
        '''
        Having [] in () for deque initialiation create a 
        temp list in deque, which acts as a 'layer' (perfect fpr BFS)
        while also making it iterable. TreeNode obj is not iterable. List 
        containing TreeNode objs are iterable. 
        '''

        while queue:
            lvl_size = len(queue)

            for i in range(lvl_size):
                node = queue.popleft()

                if i == lvl_size - 1:
                    res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res

        
