import heapq
def getSustainableCluster(processingPower:list,bootingPower:list,maxPower:int) -> int:
    
    boothq = []
    totalProcessingPower = 0
    start = 0
    clusterPower = 0
    clusterSize = 0
    maxClusterSize = 0
    for end in range(len(bootingPower) + 1):
        
        while clusterPower > maxPower:
            totalProcessingPower -= processingPower[start]
            boothq.remove(-bootingPower[start])
            heapq.heapify(boothq) #logn            
            clusterSize -= 1
            maxClusterSize = max(maxClusterSize,clusterSize)
            start += 1
            clusterPower = (boothq[0] * -1) + (totalProcessingPower) * clusterSize
        
        if end >= len(bootingPower):
            break
        
        heapq.heappush(boothq,-1 * bootingPower[end])
        totalProcessingPower += processingPower[end]
        clusterSize = (end - start) + 1
        
        clusterPower = (boothq[0] * -1) + (totalProcessingPower) * clusterSize
        
    # recalculate maxcluster in case we have got a valid one at the end
    maxClusterSize = max(maxClusterSize,clusterSize) 
    return maxClusterSize


if __name__ == "__main__":
   
    bootingPower = [4,1,4,5,3]
    processingPower = [1,2,5,3,8]
    maxPower = 30
    
    k = getSustainableCluster(processingPower,bootingPower,maxPower)
    
    print(k)
        
        
        