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

        


        print(count1)