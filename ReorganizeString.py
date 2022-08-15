"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.
"""

from queue import PriorityQueue

def reorganizeStr(s: str) -> str:
    charDict = dict()
    freqpq = PriorityQueue()
    result = ""
    
    for ch in s:
        if ch in charDict:
            charDict[ch] += 1
        else:
            charDict[ch] = 1
    
    # arrange chars in heap based on freq        
    for ch,freq in charDict.items():
        freqpq.put((freq * -1,ch))
        
    while freqpq.qsize() > 1:     
        # extract top 2 max elements from the heap
        # and alternatively append them
        max1 = freqpq.get()
        max2 = freqpq.get()
        
        result += max1[1]
        result += max2[1]
        
        if (max1[0] * -1) - 1 > 0:
            freqpq.put((max1[0] + 1,max1[1]))
        
        if (max2[0] * -1) - 1 > 0:
            freqpq.put((max2[0] + 1,max2[1]))
    
    # if the freq of the last remaining element in queue
    # is greater than 1 that means we cant organize the 
    # string return blank
    if freqpq.queue[0][0] * -1 > 1:
        return ""
    else:
        result += freqpq.get()[1]
        
    return result 

if __name__ == "__main__":
    s = "aab"
    print(reorganizeStr(s))
    s = "aaab"
    print(reorganizeStr(s))
    s = "aabcccdefcc"
    print(reorganizeStr(s))