def countBalls(l:int,h:int)->int:
    boxdict = dict()
    maxballs = 1
    for ball in range(l,h+1) :
        box = 0
        
        while ball:
            box += (ball % 10)
            ball //= 10
        
        if box in boxdict:
            boxdict[box] += 1
            maxballs = max(maxballs,boxdict[box])
        else:
            boxdict[box] = 1
    
    return maxballs

if __name__ == "__main__":
    print(countBalls(19,28))