


from math import comb
from typing import List

def doCombine(curr_n,n,k,vec,combs):
    
    if len(vec) == k:
        combs.append(vec.copy())
        return    
                 

    for i in range(curr_n,n):
        vec.append(i + 1)        
        doCombine(i + 1,n,k,vec,combs)
        vec.pop()

    return


def combine(n: int, k: int) -> List[List[int]]:
    combs = list()
    vec = list()
    
    doCombine(0,n,k,vec,combs)
    
    return combs


if __name__ == "__main__":
    ab = combine(4,2)