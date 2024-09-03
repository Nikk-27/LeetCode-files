#1046 Last Stone Weight

import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)      # takes O(n)
        while len(stones) > 1 :    # takes O(n)
            y = -heapq.heappop(stones)      # takes O(log n)
            x = -heapq.heappop(stones)      # takes O(log n)
            if x < y:
                heapq.heappush(stones, -(y - x))      # takes O(log n)
        return -stones[0] if stones else 0   # total TC = O(n log n) , SC = O(n)

stones = [2,7,4,1,8,1]
solution = Solution()
print(solution.lastStoneWeight(stones))
