from collections import Counter
import heapq

class Solution(object):
    def leastInterval(self, tasks, n):
        if n == 0:
            return len(tasks)

        task_counts = Counter(tasks)
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        intervals = 0
        while max_heap:
            temp = []
            for _ in range(n + 1):
                if max_heap:
                    temp.append(heapq.heappop(max_heap))

            for count in temp:
                if count + 1 < 0:
                    heapq.heappush(max_heap, count + 1)

            if max_heap:
                intervals += n + 1
            else:
                intervals += len(temp)

        return intervals
