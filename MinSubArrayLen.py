
def minSubArrayLen(target: int, nums: list[int]) -> int:
    start = 0
    minsz = len(nums) 
    sum = 0
    
    for i in range(len(nums)):
        
        sum += nums[i]
        
        # keep calculating min size while the sum is greater than or 
        # equal to the target
        while sum >= target:
            minsz = min(minsz, (i - start + 1))
            sum -= nums[start]
            start += 1
            
    
    return minsz if minsz != len(nums) + 1 else 0


if __name__ == "__main__":
    nums = [2,3,1,2,4,3]
    lensz = minSubArrayLen(7,nums)