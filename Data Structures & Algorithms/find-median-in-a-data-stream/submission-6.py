class MedianFinder:
    import heapq
    def __init__(self):
        self.left = []
        self.right = []
        heapq.heapify(self.left)
        heapq.heapify(self.right)
        self.even = True
        
    def addNum(self, num: int) -> None:
        if self.right:
            if self.left and self.even:
                b = -heapq.heappop(self.left)
                if num > b:
                    heapq.heappush(self.right, num)
                    heapq.heappush(self.left, -b)
                else:
                    heapq.heappush(self.right, b)
                    heapq.heappush(self.left, -num)
            else:
                a = heapq.heappop(self.right)
                if num > a:
                    heapq.heappush(self.right, num)
                    heapq.heappush(self.left, -a)
                else:
                    heapq.heappush(self.right, a)
                    heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        self.even = not self.even

    def findMedian(self) -> float:
        if self.even:
            return (self.right[0] - self.left[0]) /2
        return self.right[0]
        

        