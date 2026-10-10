class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.maxHeap = []
        self.k = k
        self.i = 0

        if nums:
            for num in nums:
                heapq.heappush(self.maxHeap, num)
                self.i += 1
                if self.i > self.k:
                    heapq.heappop(self.maxHeap)
                    self.i -= 1

            

        

    def add(self, val: int) -> int:
        heapq.heappush(self.maxHeap, val)
        self.i += 1
        if self.i > self.k:
            heapq.heappop(self.maxHeap)
            self.i -= 1
        return min(self.maxHeap)

