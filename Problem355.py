#355 Design Twitter

from typing import List

class Twitter:

    def __init__(self):
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        

    def getNewsFeed(self, userId: int) -> List[int]:
        

    def follow(self, followerId: int, followeeId: int) -> None:
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        


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