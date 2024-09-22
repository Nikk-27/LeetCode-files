#973 K Closest Points to Origin

from typing import List
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Calculate the distance for each point and store as tuple (distance, point)
        dist_points = [(math.sqrt(x**2 + y**2), [x, y]) for x, y in points]
        
        # Sort the list of points by their distance (the first element in the tuple)
        dist_points.sort(key=lambda x: x[0])
        
        # Extract the first k points (ignoring the distances)
        return [point for _, point in dist_points[:k]]
    
# Example to run the function
if __name__ == "__main__":
    solution = Solution()
    points = [[2, 2], [2, 2], [3, 3], [2, -2], [1, 1]]
    k = 4
    result = solution.kClosest(points, k)
    print(result)




        