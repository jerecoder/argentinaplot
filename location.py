#get all the hashtags mentioned in the tweets from the root hashtag
import tweepy
import json
import re
import time

ckey = "uQhKux76QIJnrSWl5WZf9A2Jn"
csecret = "XzkyLclFcqMW411YLSAKYFis94TWGQlzRtbiaYLjJlW587O0sW"
atoken = "1397193652515000333-3fv7KBftRfN13j0IgSzUTfq5HPLGUW"
asecret = "yzfeKoawixZq4rYyCVR4y8DseRBmKd1Pba9Tc0JAw5Zk0"

OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret,'access_token_key':atoken, 'access_token_secret':asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth,wait_on_rate_limit=True)

def main():
    jxc = open("fpt.txt",mode="r")
    a = jxc.read()
    arr = a.split(", ")
    it = 0
    start=time.time() 
    exp = []
    wj = open("fpt.txt",mode="a")
    wj.write("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
    for x in arr:
        it+=1
        if(it%10==0):
            print("estimated time of competion " + str((((time.time()-start)/it)*len(arr)-(time.time()-start))/3600) + " hours")
            for l in exp: 
                try:
                    wj.write(l + ", ")
                except:
                    continue
            exp = []
        u = None
        try:
            u = api.get_user(x)
        except:
            print(x)
            continue
        try:
            exp.append(u.location)
        except:
            print(x)
        
    fdt = open("fpt.txt",mode="r")
    b = fdt.read()

main()