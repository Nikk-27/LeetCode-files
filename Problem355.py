#355 Design Twitter
        
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

    def post_tweet(self, userId, tweetId):
        self.time_counter += 1
        if userId not in self.user_map:
            self.user_map[userId] = User(userId)
        user = self.user_map[userId]
        user.add_tweet(Tweet(self.time_counter, tweetId))

    def get_news_feed(self, userId):
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

# Process the commands
results = []

commands = ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
values = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]

for command, value in zip(commands, values):
    if command == "Twitter":
        twitter = Twitter()
        results.append(None)  # Initialization does not return a value
    elif command == "postTweet":
        twitter.post_tweet(value[0], value[1])
        results.append(None)  # Put does not return a value
    elif command == "getNewsFeed":
        result_value = twitter.get_news_feed(value[0])
        results.append(result_value)  # get does return a value to corresponding key
    elif command == "follow":
        twitter.follow(value[0], value[1])
        results.append(None)  # Put does not return a value
    elif command == "unfollow":
        twitter.unfollow(value[0], value[1])
        results.append(None)  # Put does not return a value

print(results)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
'''
class Tweet implements Comparable<Tweet>{
    int time;
    int tweetId;
    Tweet(int t, int id){
        time = t;
        tweetId = id;
    }
    public int compareTo(Tweet that){
        return that.time - this.time; #dec
    }
}

class User {
    int userId;
    HashSet<Integer> followers;
    List<Tweet> tweets;
    User(int userId){
        this.userId = userId;
        followers = new HashSet<>();
        tweets = new LinkedList<>();
    }
    public void addTweet(Tweet t){
        tweets.add(0,t); //insertion at the head
    }
    public void addFollower(int followeeId){
        followers.add(followeeId);
    }
    public void removeFollower(int followeeId){
        followers.remove(followeeId);
    }
}

class Twitter {
    HashMap<Integer, User> userMap;
    int timeCounter;
    public Twitter() {
        userMap = new HashMap<>();
        timeCounter = 0;
    }

    public void postTweet(int userId, int tweetId) {
        timeCounter++;
        if(!userMap.containsKey(userId)){
           userMap.put(userId, new User(userId));
        }
        User user = userMap.get(userId);
        user.addTweet(new Tweet(timeCounter, tweetId));
    }

    public List<Integer> getNewsFeed(int userId){
        if(!userMap.containsKey(userId)){
           return new ArrayList<>();
        }
        PriorityQueue<Tweet> pq = new PriorityQueue<>();
        #add self tweets + followers tweets
        User user = userMap.get(userId);
        for(int followerId : user.followers){
            int count = 0;
            for (Tweet tweet : userMap.get(followerId).tweets){
                pq.offer(tweet);
                count++;
                if(count>10){
                    break;
                }
            }
        }
        int count = 0;
        for (Tweet tweet : user.tweets){
            pq.offer(tweet);
            count++;
            if(count>10){
                break;
            }
        }
        List<Integer> res = new ArrayList<>();
        int index=0;
        while(!pq.isEmpty() && index<10){
            Tweet tweet = pq.poll();
            res.add(tweet.tweetId);
            index++;
        }
        return res;
    }

    public void follow(int follwerId, int followeeId){
        if(!userMap.containsKey(follwerId)){
           userMap.put(follwerId, new User(follwerId));
        }
        if(!userMap.containsKey(followeeId)){
           userMap.put(followeeId, new User(followeeId));
        }
        User user = userMap.get(followerId);
        user.addFollower(followeeId)
    }

    public void unfollow(int follwerId, int followeeId){
        if(!userMap.containsKey(follwerId) || !userMap.containsKey(followeeId)){
           return;
        }
        User user = userMap.get(followerId);
        user.removeFollower(followeeId)
    }
}

'''