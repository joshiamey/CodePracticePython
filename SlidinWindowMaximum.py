import collections
from typing import Collection


def maxSlidingWindow( nums: list[int], k: int) -> list[int]:
    start = 0
    maxWindowItems = []
    windowitems = collections.deque()
    start = 0
    for end in range(len(nums)):      
        while windowitems and nums[windowitems[-1]] < nums[end]:
            windowitems.pop()
            
        windowitems.append(end)
        
        if start > windowitems[0]:
            windowitems.popleft()
            
        if (end - start) + 1 == k:            
            maxWindowItems.append(nums[windowitems[0]])
            start += 1
            
    return maxWindowItems

if __name__ == "__main__":
   nums = [9,10,9,-7,-4,-8,2,-6]
   
   ans = maxSlidingWindow(nums,5)
   
   print(ans)


    

