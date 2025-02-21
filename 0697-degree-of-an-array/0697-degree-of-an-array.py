# TC = O(N)
# SC = O(N)

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # we try to reduce space complexity by taking one dict

        count_first_last = {}

        for i in range(len(nums)):
            if nums[i] not in count_first_last:
                count_first_last[nums[i]] = [0, i, i]
            count_first_last[nums[i]][0] += 1
            count_first_last[nums[i]][2] = i

        length = float('inf')

        max_freq = max(count_first_last.values(), key=lambda x : x[0])[0] # this would give the list with highest freq so out of that list we need the first element becasue that is the highest freq

        for i in count_first_last.values():
            if max_freq == i[0]:
                length = min(length, i[2] - i[1] + 1)

        return length

'''
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        length = float('inf')
        count1 = {}
        first_dict = {}
        last_dict = {}
        for i in range(len(nums)):
            if nums[i] not in first_dict:
                first_dict[nums[i]] = i
            count1[nums[i]] = 1 + count1.get(nums[i], 0)
            last_dict[nums[i]] = i

        max_freq = max(count1.values())
        for i in count1.keys():
            if count1[i] == max_freq:
                length = min(length, last_dict[i] - first_dict[i] + 1)

        return length

'''