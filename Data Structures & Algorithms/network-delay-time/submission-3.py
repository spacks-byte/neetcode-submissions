
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodeList = defaultdict(list)

        for u, v, t in times:
            nodeList[u].append((v,t))

        distance = [float("inf")] * (n + 1)
        distance[k] = 0

        heap = [(0, k)]

        while heap:
            dist, curNode = heapq.heappop(heap)

            if dist > distance[curNode]:
                continue

            distance[curNode] = dist

            for neighbour, weight in nodeList[curNode]:
                newDist = dist + weight

                if newDist < distance[neighbour]:
                    distance[neighbour] = newDist
                    heapq.heappush(heap, (newDist, neighbour))

        if float('inf') in distance[1:]:
            return -1
        return max(distance[1:])

            
