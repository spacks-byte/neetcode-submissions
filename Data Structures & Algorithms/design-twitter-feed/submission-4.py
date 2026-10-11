class Twitter:
    import heapq
    def __init__(self):
        self.time = 0
        self.tweetHistory = []
        self.followers = {}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetHistory.append((self.time, (userId,tweetId)))
        if not self.followers.get(userId, 0):
            self.followers[userId] = set([userId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if not self.followers.get(userId, 0):
            return []
        personalHistory = [x for x in self.tweetHistory if x[1][0] in self.followers[userId]]
        heapq.heapify(personalHistory)
        return [heapq.heappop(personalHistory)[1][1] for _ in range(min(10,len(personalHistory)))]

    def follow(self, followerId: int, followeeId: int) -> None:
        if not self.followers.get(followerId, 0):
            self.followers[followerId] = set([followerId])
        self.followers[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.followers.get(followerId, 0):
            self.followers[followerId].discard(followeeId)
        