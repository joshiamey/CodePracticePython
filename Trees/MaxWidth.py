"""Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes 
(the leftmost and rightmost non-null nodes), 
where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level 
are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.
"""
from collections import deque
from typing import Optional

from BuildTree import TreeNode


def widthOfBinaryTree(root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append((0,root))
        maxWidth = 0
        
        while len(queue) > 0:
            levelsz = len(queue)            
            first_idx = queue[0][0]
            last_idx = queue[-1][0]
            
            maxWidth = max(maxWidth, (last_idx - first_idx + 1))
            for i in range(levelsz):
                node_index,node = queue.popleft()
                
                if node.left is not None:
                    queue.append((2*node_index,node.left))
                
                if node.right is not None:
                    queue.append((2*node_index + 1,node.right))
                    
                            
        return maxWidth
    

if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.left = TreeNode(5)
    root.left.left.left = TreeNode(6)
   
    root.right = TreeNode(2)
    root.right.right = TreeNode(9)
    root.right.right.left = TreeNode(7)
    widthOfBinaryTree(root)