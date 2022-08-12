"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
"""

from math import sqrt
from queue import PriorityQueue


def kclosest(points:list[list[int]],k:int) -> list[list[int]]:
    
    if len(points) == 1:
        return points 
    
    result = []
    distQ = PriorityQueue()
    
    for x,y in points:
        distToOrigin = sqrt(x * x + y * y)        
        distQ.put((distToOrigin,x,y))
        
    for i in range(k):
        dist,x,y = distQ.get()        
        result.append([x,y])
        
    return result

if __name__ == "__main__":
    points = [[-5,4],[-6,-5],[4,6]]
    k = 2
    kclosest(points,k)