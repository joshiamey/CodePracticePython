def countPairs(arr, k):
  # Write your code here
  
  count = 0 
  i = 0 
  j = len(arr) - 1
  
  if k > arr[j] + arr[j - 1]:
    return 0
    
  while i < j:
    pairsum = arr[i] + arr[j]
    if pairsum == k:
      ++count
      ++i
      --j
    elif pairsum < k:
      ++i
    else:
      --j
  
  return count


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(countPairs(arr,8))