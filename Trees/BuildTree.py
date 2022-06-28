class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None 
        self.right = None

class BinaryTree:

    def __init__(self) -> None:
        pass 

    def __doBuildTree(self,nodes : list,index : int) -> TreeNode:

        if index >= len(nodes) or nodes[index] is None:
            return None

        root = TreeNode(nodes[index])

        root.left = self.__doBuildTree(nodes,2*index + 1)
        root.right = self.__doBuildTree(nodes,2*index + 2)

        return root


    def buildTree(self,nodes : list) -> TreeNode:
        return self.__doBuildTree(nodes,0)


if __name__ == "__main__":
    nodes = [1,2,5,3,4,None,6]
    tree = BinaryTree()
    
    root = tree.buildTree(nodes)
    
    print("test done")