#get all the hashtags mentioned in the tweets from the root hashtag
import tweepy
import json
import re
import time

ckey = "KnMSUuHkEC9fERQCNXnmd2WIj"
csecret = "n2ZBXrwJUY4OX8JRTCK5UePx5aWxpLmXp2ZDo1SN9RjlUIzwQl"
atoken = "1397193652515000333-mVNPIznXubMVtuIhoPBJv53bEzD3EE"
asecret = "1uONP3Olkn3hIfgsdXjA87c5fJsqYKlwzZSs9VffBKlXs"

OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret,'access_token_key':atoken, 'access_token_secret':asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth,wait_on_rate_limit=True)

def count_term(term,arr):
    times = 0
    HashTweets = tweepy.Cursor(api.search, q="#"+term).items(10)
    hlist =[tweet for tweet in HashTweets]
    #contar veces que aparece el termino en el array
    for i in hlist:
        txt = i.text
        sh =  re.findall(r"#(\w+)", txt[0:len(txt)])
        for h in sh:
            if h == term:times+=1
    return times, len(hlist)

def count_terms(tweets,previous):
    times = {}
    hashs = []
    for i in tweets:
        txt = i.text
        sh =  re.findall(r"#(\w+)", txt[0:len(txt)])
        for h in sh:
            times[h]=times[h]+1 if h in times.keys() else 1
            if not (h in previous): 
                hashs.append(h)
    return times, hashs

def main():
    # Opening JSON file
    f = open('dump.json')
    
    data = json.load(f)
    
    #pro = data["pro"]
    #op = data["op"]
    
    #export json
    exp = []
    
    # Iterating through the json
    tweet_list = []
    it = 0
    start = time.time()
    for i in data['in']:
        it+=1
        now = time.time()
        if(it%10 == 0):
            print(it)
            print("estimated time of competion " + str((((now-start)/it)*len(data['in'])-(now-start))/3600) + " hours")
            with open('dump.json', 'w') as outfile:
                json.dump(data, outfile)
        t = []
        try:
            u = api.get_user(i)
        except:
            print(i)
            continue
        if(u.protected):
            print(i)
            continue
        try:
            t.append(i)
            for status in tweepy.Cursor(api.user_timeline, id=i).items(20):
                if hasattr(status, "entities"):
                    entities = status.entities
                    if "hashtags" in entities:
                        for ent in entities["hashtags"]:
                            if ent is not None:
                                if "text" in ent:
                                    hashtag = ent["text"]
                                    if hashtag is not None:
                                        t.append(hashtag)
            data["hash"].append(t)
        except:
            print(i)
            continue

    with open('dump.json', 'w') as outfile:
        json.dump(data, outfile)

main()