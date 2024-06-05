#239 Sliding Window Maximum

# takes too much time TC = O(N*K), SC = O(K)

from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if not nums:
            return []
        if k == 1:
            return nums

        window = {}
        l = 0
        count = 0
        max_list = list()
        max_in_window = float('-inf')
        
        for r in range(len(nums)):
            window[nums[r]] = 1 + window.get(nums[r], 0)
            max_in_window = max(max_in_window, nums[r])  # Update max_in_window
            # print("window ", window)
            count += 1
            # print("count ", count)
            while count == k:
                # print(max(window.keys()))
                max_list.append(max_in_window)
                # print("^^",nums[l])
                # del window[nums[l]]
                element_out = nums[l]
                window[nums[l]] -= 1
                if window[nums[l]] == 0:
                    del window[nums[l]]
                if element_out == max_in_window:  # If the element going out was the maximum, find the new maximum
                    max_in_window = max(window.keys()) if window else float('-inf')
                count -= 1
                # print(max_list)
                l += 1
                
        return max_list
    

nums = [1,3,1,2,0,5]
k = 2
solution = Solution()
print(solution.maxSlidingWindow(nums, k))