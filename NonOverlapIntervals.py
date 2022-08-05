def eraseIntervals(intervals:list) -> int:
    # sort based on end time of the intervals
    intervals.sort(key=lambda x:x[1])
        
    curr_end = intervals[0][1]
    removed_intervals = 0
    for i in range(1, len(intervals)):
        new_start = intervals[i][0]
        new_end = intervals[i][1]
        
        if curr_end > new_start:
            removed_intervals += 1
        else:
            curr_end = new_end
    
    return removed_intervals



if __name__ == "__main__":
    eraseIntervals([[-2,2],[-1,2],[-3,4],[3,4],[-6,8]])            