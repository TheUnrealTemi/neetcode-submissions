class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        for i in range(n):
            if newInterval[0] < intervals[i][0]:
                intervals.insert(i, newInterval)
        
        if len(intervals) == n:
            intervals.append(newInterval)

        mergedInterval = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= mergedInterval[-1][1]:
                mergedInterval[-1][1] = max(mergedInterval[-1][1], intervals[i][1])
            else:
                mergedInterval.append(intervals[i])

        return mergedInterval