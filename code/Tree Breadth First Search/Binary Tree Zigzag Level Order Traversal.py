# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        search_q = deque([root])

        while search_q:

            level = []
            size = len(search_q)
            for _ in range(size):
                node = search_q.popleft()
                level.append(node.val)

                if node.left:
                    search_q.append(node.left)
                if node.right:
                    search_q.append(node.right)
            if len(result) % 2 == 1:
                level = level[::-1]

            result.append(level)
        return result



        