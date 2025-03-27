class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.result = []

    def sumRange(self, left: int, right: int) -> int:
        value = 0
        for i in range(left, right+1):
            value += self.nums[i]
        return value
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)