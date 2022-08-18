from contextlib import nullcontext
from curses.ascii import isalnum
from BuildTree import TreeNode

class PostFixTree:
    
    def buildExprTree(self,expression:list[str]) -> TreeNode:
        stack = []
        root = None
        for s in expression:
            if s.isalnum():
                node = TreeNode(int(s))
                stack.append(node)
            else:
                right_node = stack.pop()
                left_node = stack.pop()
                
                node = TreeNode(s)
                node.left = left_node
                node.right = right_node                
                stack.append(node) 
                
        root = stack.pop()
        
        return root
    
    def evaluate(self,root:TreeNode) -> int:
        
        if root is None:
            return -1
        
        left_val = self.evaluate(root.left)
        right_val = self.evaluate(root.right)
        
        
        if root.val == '+':
            return (left_val + right_val)
        elif root.val == '-':
            return (left_val - right_val)
        elif root.val == '*':
            return (left_val * right_val)
        elif root.val == '/':
            return (left_val // right_val)
        else:
            return root.val
        


if __name__ == "__main__":
    expr =  ["3","4","+","2","*","7","/"]
    pf = PostFixTree()
    
    rootNode = pf.buildExprTree(expr)
    
    expr_evaluate = pf.evaluate(rootNode)
    
    print(expr_evaluate)
    
                
                       