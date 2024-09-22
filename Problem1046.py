#1046 Last Stone Weight

import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert all stones to negative to simulate a max-heap using heapq
        stones = [-s for s in stones]
        
        # Transform the list into a heap
        heapq.heapify(stones)
        
        # Continue while there's more than one stone
        while len(stones) > 1:
            # Pop the two largest stones (negative values, so we negate them back)
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            
            # If the stones are not equal, push the difference back into the heap
            if x < y:
                heapq.heappush(stones, -(y - x))
        
        # Return the weight of the last stone, or 0 if none remain
        return -stones[0] if stones else 0

# Example to run the function
if __name__ == "__main__":
    solution = Solution()
    stones = [2, 7, 4, 1, 8, 1]
    result = solution.lastStoneWeight(stones)
    print(f"The last stone weight is: {result}")
