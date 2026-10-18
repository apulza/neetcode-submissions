class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count frequency of each number -> O(n)
        count = Counter(nums)

        # create buckets where index = frequency -> O(n)
        # array size is len(nums) + 1 since a number can appear up to len(nums) times
        freq = [[] for _ in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)

        # gather top k elements from highest frequency down -> O(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res