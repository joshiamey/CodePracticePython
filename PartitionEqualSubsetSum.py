"""
Given a non-empty array nums containing only positive integers, 
find if the array can be partitioned into two subsets 
such that the sum of elements in both subsets is equal. 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""


def doCanPart(nums: list[int],target:int,index:int) -> bool :
    
    if target < 0 or index < 0:
        return False
        
    if not target:
        return True
    
    return doCanPart(nums,target - nums[index],index - 1) or doCanPart(nums,target,index - 1)
    
    
def canPartition(nums: list[int]) -> bool:
    
    sum = 0
    for num in nums:
        sum += num
        
    if sum % 2 != 0:
        return False
    
    sum /= 2
    
    # memo = [[False] * sum]*len(nums)
    
    # for i in range(1,sum + 1):
    #     for j in range(len(nums)):            
    #         memo[i][j] = memo[i - nums[j]][j - 1] or memo[i][j-1]
    return doCanPart(nums,sum,len(nums) - 1)

if __name__ == "__main__":
    
    print(canPartition([1,5,10]))
    