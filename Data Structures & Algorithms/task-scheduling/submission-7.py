class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import deque
        import heapq

        hashmap = {}
        for task in tasks:
            hashmap[task] = hashmap.get(task, 0) + 1
        tasksMap = [-qty for qty in hashmap.values()]
        heapq.heapify(tasksMap)

        cooldownQueue = deque()

        time = 0
        while tasksMap or cooldownQueue:
            time += 1
            if cooldownQueue:
                peek = cooldownQueue[0]
                if peek[1] == time:
                    cur = cooldownQueue.popleft()
                    heapq.heappush(tasksMap, cur[0])

            if tasksMap:
                cur = heapq.heappop(tasksMap)
                if cur != -1:
                    cooldownQueue.append(((cur)+1, time+n+1))

        return time
                




        