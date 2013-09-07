'''
Created on Aug 29, 2013, modified on 9/6/2013
@author: vandana, extended by Jeremy Cantu
Processes the tweets file to get the details from the tweets
'''

import json
import gzip

def get_tweets(in_file):
  tweets  = []
  f = gzip.open(in_file, "r")
  #f = open(in_file, "r")
  for line in f:
    #print line
    data = json.loads(line)
    #short_tweet = {"text": data["text"], "id": data["id"]}
    tweets.append(data)
  f.close()
  return tweets

def print_tweets_structure(tweet_dict, tab_level=0):
  for i in tweet_dict:
    tab_string = "\t"*tab_level if tab_level > 0 else ""
    print tab_string + i
    if type(tweet_dict[i]) is dict:
      print_tweets_structure(tweet_dict[i], tab_level+1)

if __name__ == "__main__":
  in_file = "/home/vandana/workspace/Dropbox/codinggig/data/sample/geo.2013-08-26_23-45.txt"
  tweets = get_tweets(in_file)
