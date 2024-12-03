class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        single_zero = False
        multi_zero = False
        n = len(nums)
        result = [1] * n
        prefix_product = 1
        postfix_product = 1

        for num in nums:
            if single_zero and num == 0 :
                multi_zero = True
                single_zero = False
                break
            if num == 0 :
                single_zero = True
            else:
                p *= num

        # print(single_zero, multi_zero)
        if multi_zero : 
            for i in range(n):
                result[i] = 0
                continue
        if single_zero :
            for i in range(n):
                if nums[i] != 0 :
                    result[i] = 0
                else:
                    result[i] = p
        else:
            for k in range(n):
                result[k] *= prefix_product
                prefix_product *= nums[k]
                # print("1.", result)
                # print("prefix_product ", prefix_product)
                # print("++++++++")
                # print("\n")
            for j in range(n - 1, -1, -1):
                result[j] *= postfix_product
                postfix_product *= nums[j]
                # print("2.", result)  
                # print("postfix_product ", postfix_product)
                # print("$$$$$$$$$$$$$$")
                # print("\n")
        return result 
