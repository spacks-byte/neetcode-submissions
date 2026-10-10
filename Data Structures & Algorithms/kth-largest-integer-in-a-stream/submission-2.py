class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k
        self.i = 0

        if nums:
            for num in nums:
                heapq.heappush(self.minHeap, num)
                self.i += 1
                if self.i > self.k:
                    heapq.heappop(self.minHeap)
                    self.i -= 1

            

        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        self.i += 1
        if self.i > self.k:
            heapq.heappop(self.minHeap)
            self.i -= 1
        return self.minHeap[0]

