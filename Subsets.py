
def doSubsets(nums: list[int],index:int,currset:list[int],subsets:list[list[int]]):
    # append the current set copy to larger list
    subsets.append(currset.copy())

    if index >= len(nums):
        return
    
    
    for j in range(index,len(nums)):
        # append the element to the set and then recurse on remaining nums
        currset.append(nums[j])
        doSubsets(nums,j + 1,currset,subsets)
        # we pop the last appended element after that path is processed
        # that way 
        currset.pop()
    

def subsets(nums : list[int]) -> list:
    currset = []
    subsetlist = []
    
    doSubsets(nums,0,currset,subsetlist)
    
    return subsetlist


if __name__ == "__main__":
    nums = [1,2,3]
    
    subset = subsets(nums)
    
    print(subset)