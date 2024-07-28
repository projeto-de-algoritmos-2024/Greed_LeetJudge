class Solution:
    def eraseOverlapIntervals(self, intervals):

        def getEndTime(interval):
            return interval[1]
        
        intervals.sort(key=getEndTime) 

        scheduledCount = 1
        start, end = intervals[0]

        for s, e in intervals:
            if s < end:
                continue
            else:
                start, end = s , e
                scheduledCount += 1
        
        return len(intervals) - scheduledCount
