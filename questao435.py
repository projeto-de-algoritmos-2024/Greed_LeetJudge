class Solution:
    def eraseOverlapIntervals(self, intervals):

        # Ordenar os pontos pelo fim do intervalo
        intervals.sort(key=lambda x:x[1]) 

        scheduledCount = 1 # Conta quantas tarefas são agendadas sem conflito
        start, end = intervals[0]

        for s, e in intervals:
            if s < end:
                continue
            else:
                start, end = s , e
                scheduledCount += 1
        
        return len(intervals) - scheduledCount
