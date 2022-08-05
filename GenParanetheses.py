def generateParenthesis(n: int) -> list[str]:
    strlist = []
    
    def doGenParen(openP,closeP,n,s):
        
        if openP == n and closeP == n:
            strlist.append(s)
            return
        
        # add open bracket as its less than n
        if openP < n:
            doGenParen(openP+1,closeP,n,s+"(")
            # backtrack

        # only add the closing bracket if its less than open bracket count
        if closeP < openP:
            doGenParen(openP,closeP+1,n,s+")")
            
        return
            
    
    doGenParen(0,0,n,"")
    
    return strlist

if __name__ == "__main__":
    generateParenthesis(2)