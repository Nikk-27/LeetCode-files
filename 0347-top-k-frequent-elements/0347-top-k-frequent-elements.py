class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_n = {}
        for n in nums:
            count_n[n] = 1 + count_n.get(n, 0)
        heap = []
        res = []

        for n, cnt in count_n.items():
            heapq.heappush(heap, [cnt, n])
            if len(heap) > k:
                heapq.heappop(heap)

        for n in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

# TC = O(n + logk)
# SC = O(n+k)

