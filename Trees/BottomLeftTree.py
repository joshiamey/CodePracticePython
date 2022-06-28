from curses.panel import bottom_panel
from typing import Optional
from collections import deque
import BuildTree
bottomleft = 0
valdict = dict()

def findBottomLeftValue(root:Optional[BuildTree.TreeNode]) -> int:
    queue = deque();
    queue.append(root);
    bottomLeft = -1;
    
    while len(queue) > 0:
        level = len(queue)
       
        for i in range(level):
            node = queue.popleft()
            if node.right is not None:
                queue.append(node.right)
            
            if node.left is not None:
                queue.append(node.left)
                
            if i is level - 1:
                bottomLeft = node.val
                
    return bottomLeft

def doFindBottomLeftVal(root:BuildTree.TreeNode,level:int):
    if root is None:
        return 
    
    if level not in valdict:
        valdict[level] = root.val;
        bottomleft = root.val;
        
    doFindBottomLeftVal(root.left,level+1)
    doFindBottomLeftVal(root.right,level+1)
    
    return
    
    
if __name__ == "__main__":
    nodes = [1,2,3,4,None,5,6,None,None,None,None,7]
    tree = BuildTree.BinaryTree()
    
    root = tree.buildTree(nodes)
    
    # val = findBottomLeftValue(root);
    doFindBottomLeftVal(root,0)

    
                
                
    
    