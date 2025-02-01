class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) ==  1:
            return nums[0]

        t = [0] * (len(nums)+1)
        n = len(t)

        t[0] = 0

        for i in range(1, n-1):
            skip = t[i-1]
            steal = nums[i-1] + (t[i-2] if (i-2 >= 0) else 0)
            t[i] = max(skip, steal)
            print(t[i])
        result1 = t[n-2]
        
        t = [0] * (len(nums)+1)
        t[0] = 0
        t[1] = 0 #since we are taking last house we have to skip 1st house
        for i in range(2, n):
            skip = t[i-1]
            steal = nums[i-1] + (t[i-2] if (i-2 >= 0) else 0)
            t[i] = max(skip, steal)
        result2 = t[n-1]

        return max(result1, result2)


# if house 1 taken then skip last
# else if house 1 skipped then take last house
# thats how we have two for loops

# TC = O(n) + O(n)
# SC = O(n)