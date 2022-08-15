from queue import PriorityQueue


def freqSort(s:str) -> str:
    result = ""
    charDict = dict()
    freqPq = PriorityQueue()
    
    for ch in s:
        if ch in charDict:
            charDict[ch] += 1
        else:
            charDict[ch] = 1
    
    
    for ch,freq in charDict.items():
        freqPq.put((freq * -1,ch))
        
    while freqPq.qsize() > 0:
        freq,ch = freqPq.get()        
        result += ch * (freq * -1)
        
    return result

if __name__ == "__main__":
    s = "dehgLmnmadaecef"
    print(freqSort(s))