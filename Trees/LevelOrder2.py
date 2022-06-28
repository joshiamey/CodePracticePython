

from typing import List, Optional
from BuildTree import TreeNode


class Solution:
    def __init__(self):
        self.order = list()
        
    def __doLevelOrderBottom(self,root:TreeNode,level:int):
        if root is None:
            return
        
        if len(self.order) <= level:
            self.order.append([])
            
        self.order[level].append(root.val)               
        self.__doLevelOrderBottom(root.left,level+1)
        self.__doLevelOrderBottom(root.right,level+1)
        
        return
        
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        self.__doLevelOrderBottom(root,0)
        
        return self.order.reverse()      
    

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(15)
    
    sol = Solution()
    ans = sol.levelOrderBottom(root)
    print(ans)