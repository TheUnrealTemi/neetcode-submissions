"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        
        intervals.sort(key = lambda i : i.start)
        result = 1
        heap = [intervals[0].end]
        
        for i in range(1, len(intervals)):
            if heap[0] <= intervals[i].start:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)
            result = max(result, len(heap))
            
        return result