from typing import List, Optional
from BuildTree import TreeNode
from collections import deque

def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    
    nodeq = deque()
    nodeq.append(root)
    zigzag = list()
    level = 0
    
    while len(nodeq) > 0:
        levelsz = len(nodeq)
        # pre-allocate the list based on the size            
        levelorder = levelsz * [0]        
        isOdd = (level % 2)
        it = 0
        increment = 1
        if isOdd: # if its odd level , start filling from the end
            it = levelsz - 1
            increment = -1
            
        for i in range(levelsz):                
            node = nodeq.popleft()
            levelorder[it] = node.val
            it += increment
                
            if node.left:
                nodeq.append(node.left)
            if node.right:
                nodeq.append(node.right)
        
        level += 1
        zigzag.append(levelorder)
            
            
    return zigzag


