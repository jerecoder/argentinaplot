#get all the hashtags mentioned in the tweets from the root hashtag
from numpy.random import f
import tweepy
import json
import re
import time
import csv
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
import pandas
import tweepy

ckey = "uQhKux76QIJnrSWl5WZf9A2Jn"
csecret = "XzkyLclFcqMW411YLSAKYFis94TWGQlzRtbiaYLjJlW587O0sW"
atoken = "1397193652515000333-3fv7KBftRfN13j0IgSzUTfq5HPLGUW"
asecret = "yzfeKoawixZq4rYyCVR4y8DseRBmKd1Pba9Tc0JAw5Zk0"

OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret,'access_token_key':atoken, 'access_token_secret':asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth,wait_on_rate_limit=True)

def main():
    data = pandas.read_csv("ds.csv", header=None,delimiter=",")
    target = []
    n = int(len(data)/2)
    for x in range(n):
        target.append(0)
    for x in range(n):
        target.append(1)
    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.3,random_state=109) # 70% training and 30% test
    #Create a svm Classifier
    clf = svm.SVC(kernel='linear') # Linear Kernel

    #Train the model using the training sets
    clf.fit(X_train, y_train)

    #Predict the response for test dataset
    predict = pandas.read_csv("m.csv",header=None,delimiter=",")
    y_pred = clf.predict(predict)
    f = 0
    c = 0
    fpt = []
    jxc = []
    lis = list(csv.reader(open("users.csv")))
    for x in range(len(y_pred)):
        if(y_pred[x]):
            f+=1
            fpt.append(lis[f+c-1][0])
        else:
            c+=1
            jxc.append(lis[f+c-1][0])
    jxcf = open("jxc.txt","a")#append mode
    fptf = open("fpt.txt","a")#append mode
    for x in fpt:
        fptf.write(x + ", ")
    for y in jxc:
        jxcf.write(y + ", ")

    #print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
main()