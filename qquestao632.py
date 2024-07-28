import heapq

class Solution:
    def smallestRange(self, nums):

        n = len(nums)
        
        heap = [(num[0], i, 0) for i, num in enumerate(nums)]
        heapq.heapify(heap)
        
        max_val = max(num[0] for num in nums)
        
        start, end = 0, float('inf')
        
        while len(heap) == n:
            val, i, j = heapq.heappop(heap)
            
            if end - start > max_val - val:
                start, end = val, max_val
            
            if j + 1 < len(nums[i]):
                heapq.heappush(heap, (nums[i][j + 1], i, j + 1))
                max_val = max(max_val, nums[i][j + 1])
        
        return [start, end]
