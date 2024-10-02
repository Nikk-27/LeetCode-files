import heapq
from collections import defaultdict, deque

class Tweet:
    def __init__(self, time, tweetId):
        self.time = time
        self.tweetId = tweetId

    def __lt__(self, other):
        return self.time > other.time  # Max heap in Python uses min heap by default, so reverse the comparison

class User:
    def __init__(self, userId):
        self.userId = userId
        self.followers = set()
        self.tweets = deque()  # Use deque for efficient head insertion

    def add_tweet(self, tweet):
        self.tweets.appendleft(tweet)  # Add tweet at the head

    def add_follower(self, followeeId):
        self.followers.add(followeeId)

    def remove_follower(self, followeeId):
        self.followers.discard(followeeId)

class Twitter:
    def __init__(self):
        self.user_map = defaultdict(User)  # Automatically creates User if not present
        self.time_counter = 0

    def postTweet(self, userId, tweetId):
        self.time_counter += 1
        if userId not in self.user_map:
            self.user_map[userId] = User(userId)
        user = self.user_map[userId]
        user.add_tweet(Tweet(self.time_counter, tweetId))

    def getNewsFeed(self, userId):
        if userId not in self.user_map:
            return []
        
        pq = []
        user = self.user_map[userId]

        # Add tweets of followers
        for followerId in user.followers:
            count = 0
            for tweet in self.user_map[followerId].tweets:
                heapq.heappush(pq, tweet)
                count += 1
                if count >= 10:
                    break

        # Add own tweets
        count = 0
        for tweet in user.tweets:
            heapq.heappush(pq, tweet)
            count += 1
            if count >= 10:
                break

        # Get the top 10 most recent tweets
        res = []
        while pq and len(res) < 10:
            tweet = heapq.heappop(pq)
            res.append(tweet.tweetId)
        
        return res

    def follow(self, followerId, followeeId):
        if followerId not in self.user_map:
            self.user_map[followerId] = User(followerId)
        if followeeId not in self.user_map:
            self.user_map[followeeId] = User(followeeId)

        self.user_map[followerId].add_follower(followeeId)

    def unfollow(self, followerId, followeeId):
        if followerId not in self.user_map or followeeId not in self.user_map:
            return
        self.user_map[followerId].remove_follower(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)