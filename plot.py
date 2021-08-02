#get all the hashtags mentioned in the tweets from the root hashtag
import tweepy
import json
import re
import time

ckey = "KnMSUuHkEC9fERQCNXnmd2WIj"
csecret = "n2ZBXrwJUY4OX8JRTCK5UePx5aWxpLmXp2ZDo1SN9RjlUIzwQl"
atoken = "1397193652515000333-S2vj1iEYR3zS0YGgeLTWcpC9pdgcds"
asecret = "lBh7GVkzxqkOhIOXtjpPSVmmHH7yvUUG0yptE3uWNuYpm"

OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret,'access_token_key':atoken, 'access_token_secret':asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth,wait_on_rate_limit=True)

def main():
    # Opening JSON file
    f = open('argentinaplot/dump.json')
    
    data = json.load(f)
    
    #pro = data["pro"]
    #op = data["op"]
    
    #export json
    exp = []
    
    # Iterating through the json
    tweet_list = []
    for i in data['hash-dump']:
        HashTweets = tweepy.Cursor(api.search, q="#"+i).items(40)
        locations = []
        for x in HashTweets:
            l = x.user.location
            if ((l not in locations) and len(l)>0 ) : locations.append(l)
        count = 0
        for x in locations:
            x.lower()
            arg = False
            for y in data["locations"]:
                if (arg == True) : 
                    break
                y.lower()
                if(x.find(y)!=-1):arg = True
            if (arg == True) : count += 1
        if(count == 0 or len(locations) == 0):continue
        fidelity = count/len(locations);
        if(fidelity > 0.5):exp.append(i)
    
    data["hash-dump"]=exp
    with open('argentinaplot/dump.json', 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

main()