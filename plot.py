#get all the hashtags mentioned in the tweets from the root hashtag
import tweepy
import json
import re
import time
import csv
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
import pandas

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
    y_pred = clf.predict(X_test)
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
main()