class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())


Time & Space Complexity
Time complexity: O(m∗nlogn)
Space complexity: O(m∗n)
Where m is the number of strings and n is the length of the longest string.
