
def doSubsets(nums: list[int],j:int,currset:list[int],subsets:list[list[int]]):
    # append the current set copy to larger list
    if j == len(nums):
        subsets.append(currset.copy())
        return 
    
    # append the element to the set and then recurse on remaining nums
        
    currset.append(nums[j])
    doSubsets(nums,j + 1,currset,subsets)
    # we pop the last appended element after that path is processed
    # that way 
    currset.pop()
    while j + 1 < len(nums) and (nums[j] == nums[j + 1]): 
        j += 1    
    doSubsets(nums,j + 1,currset,subsets)

    

def subsets(nums : list[int]) -> list:
    currset = []
    subsetlist = []
    nums = sorted(nums)
    doSubsets(nums,0,currset,subsetlist)
    
    return subsetlist


if __name__ == "__main__":
    # nums = [1,2,2]
    
    # subset = subsets(nums)
    
    # print(subset)\
    s = "abcd"
    print(s)
    s.pop
    print(s)