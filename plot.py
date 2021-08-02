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
    for i in data['hash-dump']:
        print("hash"+i)
        HashTweets = tweepy.Cursor(api.search, q="#"+i).items(30)
        tweet_list.append([tweet for tweet in HashTweets])
    
    for ind in range(len(tweet_list)):
        #buscar todos los hashtags que son derivados de un hashtag base
        times, hashs = count_terms(tweet_list[ind],{x for x in data["hash-dump"] or x in exp or x in data["past"]})
        #sumar a la lista final los que tienen coeficiente de Jaccard mayor a 0.005
        for h in hashs:
            timesi,size = count_term(h,data["hash-dump"][ind])
            if((times[h]+timesi*3)/(len(tweet_list[ind])+size*3) >= 0.1 and not (h in exp)):exp.append(h)

    
    data["past"].extend(data["hash-dump"])
    data["hash-dump"]=exp
    with open('dump.json', 'w') as outfile:
        json.dump(data, outfile)

main()