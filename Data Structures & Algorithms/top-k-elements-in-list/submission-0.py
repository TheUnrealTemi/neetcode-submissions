import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for num in nums:
            dic[num] = dic.get(num, 0) +1

        heap = []

        for key, val in dic.items():
            if len(heap) < k or val > heap[0][0]:
                heapq.heappush(heap, [val, key])
            if len(heap) > k:
                heapq.heappop(heap)

        return [i[1] for i in heap]
