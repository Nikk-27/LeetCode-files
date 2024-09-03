#703 Kth Largest Element in a Stream

import heapq
from typing import Optional, List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = nums
        heapq.heapify(self.minheap)      # takes O(n)
        while len(self.minheap) > self.k:   #runs for O(n-k) times
            heapq.heappop(self.minheap)     # takes O(log n) for each pop operation because size of heap is n here
                                            # TC = O(n + (n-k).log n), SC = O(k)
    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)  # O(log k) because size of heap is k here
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)    # O(log k) because size of heap is k here
        return self.minheap[0]             # TC = O(log k), SC = O(k)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

commands = ["KthLargest","add","add","add","add","add"]
values = [[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
results = list()


for command, value in zip(commands, values):
    if command == "KthLargest":
        heap_queue = KthLargest(value[0], value[1])
        results.append(None)  # Initialization does not return a value
    elif command == "add":
        max_element = heap_queue.add(value[0]) 
        print(max_element)
        results.append(max_element)

print(results)
    