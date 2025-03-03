class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        a_list = [0] * len(piles)
        # print("h: ", h)
        for temp in range(1, max(piles)+1):
            piles_copy = piles.copy()
            # print("piles_copy: ", piles_copy)
            # print("temp: ", temp)
            # print("______________________")
            for i in range(h):
                # print("i: ", i)
                for j in range(len(piles_copy)):
                    if piles_copy[j] > 0:
                        piles_copy[j] = piles_copy[j] - temp
                        if piles_copy[j] < 0:
                            piles_copy[j] = 0
                            # if a_list == piles_copy:
                                # print(temp)
                        # print("piles_copy after: ", piles_copy)
                        if piles_copy == a_list:
                            return temp
                        else:
                            break
        '''#runs good but exceeds time limit

        l, r = 1, max(piles) # TC : O(NLogM), SC : O(1)   -> O(max(P).P) we will use BS therefore O(log(max(P)).P) M = maximum number of bananas in a pile
        res = r

        while l <= r:
            k = l + ((r - l) // 2) # Overflow-Safe Middle Calculation
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res

        
                


