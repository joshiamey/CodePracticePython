def findlen(nums1,nums2) -> int:
    m = len(nums1) - 1
    n = len(nums2) - 1
    def dofindlen(nums1,nums2,i,j) ->int:
        if i < 0 or j < 0:
            return 0
        
        if nums1[i] == nums2[j]:
            return 1 + dofindlen(nums1,nums2,i-1,j-1)
        
        return max(dofindlen(nums1,nums2,i,j-1),dofindlen(nums1,nums2,i-1,j))
    
    return dofindlen(nums1,nums2,m-1,n-1)
    