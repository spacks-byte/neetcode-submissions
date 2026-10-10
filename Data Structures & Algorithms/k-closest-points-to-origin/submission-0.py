class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        from math import sqrt
        heap = [((sqrt(x1**2 + y1**2)), i) for i, (x1, y1) in enumerate(points)]
        print(heap)
        heapq.heapify(heap)
        final = []
        for i in range(k):
            final.append(points[heapq.heappop(heap)[1]])
        
        return final
        