#621 Task Scheduler

from typing import List
import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Create a frequency map of tasks
        freq_map = Counter(tasks)
        
        # Max heap to store task frequencies
        max_heap = [-freq for freq in freq_map.values()]
        heapq.heapify(max_heap)
        
        time = 0
        
        # Process the tasks until the heap is empty
        while max_heap:
            temp = []
            cycle_tasks = 0
            for _ in range(n + 1):
                if max_heap:
                    freq = heapq.heappop(max_heap)
                    cycle_tasks += 1  # Count this as a processed task
                    if freq + 1 < 0:  # Decrease frequency and re-add if tasks remain
                        temp.append(freq + 1)
                
            
            # Push the remaining tasks back into the heap
            for freq in temp:
                heapq.heappush(max_heap, freq)
            
            # If tasks remain in the heap, this means there is a gap, so time += p + 1
            if max_heap:
                time += n + 1
            else:
                time += cycle_tasks
            print(time)
        
        return time
        

solution = Solution()
tasks = ["A","A","A","B","B","B"] 
n = 2
print(solution.leastInterval(tasks, n))  # Output: 5




