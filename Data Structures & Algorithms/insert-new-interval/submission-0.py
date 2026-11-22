class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        for i in range(n):
            if newInterval[0] < intervals[i][0]:
                intervals.insert(i, newInterval)
        if len(intervals) == n:
            intervals.append(newInterval)

        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
            
        return result