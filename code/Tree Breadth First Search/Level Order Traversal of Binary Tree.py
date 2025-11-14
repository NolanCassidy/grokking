# https://leetcode.com/problems/binary-tree-level-order-traversal/

from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        result = []
        q = deque([root])
        
        while q:
            level = []
            size = len(q)
            
            for _ in range(size):      # process exactly 1 level
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            result.append(level)       # store the full level
        
        return result