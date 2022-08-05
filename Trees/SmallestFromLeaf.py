import BuildTree

def smallestFromLeaf(root:BuildTree.TreeNode) -> str:
    
    if not root:
        return ""
    
    lhStr = smallestFromLeaf(root.left)    
    rhStr = smallestFromLeaf(root.right)
    
    rootchr = chr(root.val+97)
    if not len(lhStr) and not len(rhStr):
        return "" + rootchr    
    elif not len(lhStr) and len(rhStr):
        return rhStr + rootchr    
    elif len(lhStr) and not len(rhStr):
        return lhStr + rootchr    
    else:        
        if len(lhStr) == len(rhStr):
            if lhStr < rhStr:
                return lhStr + rootchr
            else:
                return rhStr + rootchr
        elif len(lhStr) < len(rhStr):
            return lhStr + rootchr
        else:
            return rhStr + rootchr
        