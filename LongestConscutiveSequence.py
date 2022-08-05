
def longestConsecutive(nums:list[int]) -> int:
        max_seq_cnt = 0
        nums.sort()
        curr_seq = 1
        for i in range(len(nums) - 1):
            if nums[i+1] == (nums[i] + 1):
                curr_seq += 1
            else:
                max_seq_cnt = max(curr_seq,max_seq_cnt)
                curr_seq = 1
        
        return max_seq_cnt

if __name__ == "__main__":
    
    print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))