
res = list()
def doGameScoring(arr:list,score,index,vec:list):
    if score < 0:
        return 
    
    if score == 0:
        res.append(vec.copy())
        return 
    
    for i in range(index,3):
        score -= arr[i]
        vec.append(arr[i])
        doGameScoring(arr,score,i,vec)
        vec.pop()
        score += arr[i]
        
    return
 
    
    

def gameScoring(score:int)->list[list:int]:
    vec = []
    points = [1,2,3]
    
    
    for i in range(3):
        points[0],points[i] = points[i],points[0]
        doGameScoring(points,score,0,vec)  
        points[0],points[i] = points[i],points[0]  
    
    
    return res 


if __name__ == "__main__":
    gameScoring(3)