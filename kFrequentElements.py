"""Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""
import heapq
from queue import PriorityQueue

def topKFrequent(nums:list[int], k:int) -> list[int]:
    freq = dict()
    result = []
    maxfreq = 0
    for x in nums:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
        maxfreq = max(maxfreq,freq[x])
    
    if maxfreq > 1:
        heap = PriorityQueue()

        for key,value in freq.items():
            heap.put((value * -1,key))
            
        for i in range(k):                
            value,key = heap.get()
            result.append(key)
    else:
        for i in range(k):                
            result.append(nums[i])                

    return result

if __name__ == "__main__":
    points = [5,3,1,1,1,3,73,1]
    k = 2
    topKFrequent(points,k)