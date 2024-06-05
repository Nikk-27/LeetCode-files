from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        max_list = []
        window = deque()  # Deque to store indices of elements in the current window

        for i, num in enumerate(nums):
            # Remove elements from the front of the deque that are outside the current window
            while window and window[0] <= i - k:
                print("window[0] ", window[0])
                window.popleft()

            # Remove elements from the back of the deque that are smaller than the current element
            while window and nums[window[-1]] < num:
                print("window[-1] ", window[-1])
                window.pop()

            window.append(i)  # Add the index of the current element to the deque
            print("I")
            print(i, window)

            # If the window has reached size k, add the maximum to the result list
            if i >= k - 1:
                print("inside")
                print(window[0])
                max_list.append(nums[window[0]])
                print("max_list ", max_list)

        return max_list


nums = [1,3,-1,-3,5,3,6,7]
k = 3
solution = Solution()
print(solution.maxSlidingWindow(nums, k))