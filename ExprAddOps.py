"""
Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

 

Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
(Time limit exceeded solution)
"""

ops = ['','+','-','*']

def evaluateExpr(expr:str,target):
    operand = []
    
    op = '+'   
    i = 0 
    while i < len(expr):
        
        if expr[i].isdigit():
            num = 0
            
            if i+1 < len(expr) and expr[i] == '0' and expr[i+1].isdigit():
                return False
            
            while i < len(expr) and expr[i].isdigit():
                c = int(expr[i])
                num = (num * 10) + c
                i += 1
            
            i -= 1
            
            if op == '*':
                b = num 
                a = operand.pop()
                operand.append(a*b)
            elif op == '-':
                b = num
                operand.append(b * -1)
            elif op == '/':
                b = num 
                a = operand.pop()
                if b == 0: 
                    return False
                else:
                    operand.append(a//b) 
            else:
                operand.append(num)
        else:            
            op = expr[i]
        
        i += 1
        
    ans = 0
    while len(operand) > 0:
        ans += operand.pop()
    
    return ans == target
    
    
def doAddOperators(num,i,answer,target,anslist):
    if i+1 >= len(num):    
        expr = ''.join(answer) + num[i]
        if evaluateExpr(expr,target):
            anslist.append(expr)   
                 
        return 
    
    answer.append(num[i])
    for op in ops:
        answer.append(op)        
        doAddOperators(num,i+1,answer,target,anslist) 
        answer.pop()
    
    answer.pop()
    return
        
               

def addOperators(num,target) -> list[str]:
    result = [] 
    s = []
    doAddOperators(num,0,s,target,result)
    return result


if __name__ == "__main__":
    num = "105"
    target = 5
    ans = addOperators(num,target)
    # evaluateExpr('2*3/2',6)
    
    print(ans)
    
