class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        cursum = 0
        totalsum = 0
        n = len(customers)

        for i in range(minutes):
            cursum += customers[i] * grumpy[i]  # this takes sum when owner is grumpy for first interval 0,1,2

        totalsum += cursum

        # now we move our interval ahead one at a time
        j = minutes # because we already calculated till minutes - 1
        i = 0

        while j < n:
            cursum += customers[j] * grumpy[j]  # adding right side from window
            cursum -= customers[i] * grumpy[i]  # removing left side from window
            if cursum > totalsum:  # if new window had better sum then replace new sum
                totalsum = cursum

            j += 1
            i += 1

        for i in range(n):    # now add customers where owner was not grumpy
            totalsum += customers[i] * (1 - grumpy[i])

        return totalsum


'''
# this solution works, I wrote this but it exceeds the time limit 74/78 test cases passed

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        arr = {}
        return_final_sum = 0

        for i in range(len(customers) - minutes + 1):
            current_sum = 0
            for j in range(minutes):
                current_sum += customers[i + j]

            arr[(i, i + j)] = [current_sum, i, i + j]
        

        for i in arr.values():
            final_sum = 0
            max_sum = i[0]
            start_ind = i[1]
            end_ind = i[2]

            final_sum += max_sum

            for j in range(0, start_ind):
                final_sum += customers[j] if grumpy[j] != 1 else 0

            for k in range(end_ind+1, len(customers)):
                final_sum += customers[k] if grumpy[k] != 1 else 0

            return_final_sum = max(return_final_sum, final_sum)

        return return_final_sum

        
'''