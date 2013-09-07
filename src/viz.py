'''
For a simple visualization using d3
'''
from tweets_processor import get_tweets
import json
import os
import sys
import csv

def count_expressions(tweets):
        expressions_hash = {"Bomb": {"pic": "Bomb", "val": 0},
                      "Kill": {"pic": "Kill", "val": 0},
                      "Stab": {"pic": "Stab", "val": 0},
                        "Death": {"pic": "Death", "val": 0},
                        "Shooting" : {"pic": "Shooting", "val": 0}
                     }
        for t in tweets:
                if "text" in t:
                        if "Bomb" in t["text"] or "bomb" in t["text"] or "bombed" in t["text"] or "bombing" in t["text"] or "bomber" in t["text"]:
                                expressions_hash["Bomb"]["val"] += 1
                        elif "Kill" in t["text"] or "killed" in t["text"] or "murder" in t["text"] or "murdered" in t["text"] or "murdering" in t["text"]:
                                expressions_hash["Kill"]["val"] += 1
                        elif "Stab" in t["text"] or "stab" in t["text"] or "stabbing" in t["text"] or "stabbed" in t["text"] or "shiv" in t["text"]:
                                expressions_hash["Stab"]["val"] += 1
                        elif "Dead" in t["text"] or "dead" in t["text"] or "death" in t["text"]:#or "dying" in t["text"]:
                                expressions_hash["Death"]["val"] += 1
                        elif "Shooting" in t["text"] or "Shot" in t["text"] or "Shoot" in t["text"] or "shoot" in t["text"]:# or "shot" in t["text"]:
                                expressions_hash["Shooting"]["val"] +=1
        f = open("exprs.json", "w")
        expressions = []
        for a in expressions_hash:  
                expressions.append(expressions_hash[a])
        f.write(json.dumps(expressions))
        f.close()
        print expressions_hash

def count_expressions_two(tweets):
    csvfile = file("coords.csv", "w")
    csvwriter = csv.writer(csvfile)
    row = ['lat', 'lon']
    csvwriter.writerow(row)
    for t in tweets:
        if 'coordinates' in t:
            coord = str(t['coordinates'])
            coord = coord[34:-2]
            if len(coord) > 9:
                x, _, y = coord.rpartition(', ')
                try:
                    lat = float(x)
                    lng = float(y)
                except ValueError,e:
                    print"error",e
                #print lat, lng
                row = [lat, lon]
                csvwriter.writerow(row)
    #out = open("coords.csv", "w")
    #print >> out, 'lat,lon'
    #rows = zip(lat, lon)
    #from csv import writer
    #csv = writer(out)
    #for row in rows:
     #   values = [(value.encode('utf8') if hasattr(value, 'encode') else value) for value in row]
      #  csv.writerow(values) 
    csvfile.close()
        #f = open("coords.json", "w")
        #coordinates = []
        #for a in expressions_hash:  
        #        expressions.append(expressions_hash[a])
        #f.write(json.dumps(coordinates))
        #f.close()
        #print expressions_hash


def main():
        #in_file = "C:\Users\Jac21ASUS\Documents\~School2012\CSCE 221\WORK\CodingGig_2013\data\sample\geo.2013-08-26_23-45.txt"
        #in_file = os.getcwd() + "geo.2013-08-26_23-45.txt"
        all_tweets = []
        for root, dirs, files in os.walk("2013_1_1"):
            for fname in files:
                print fname
                in_file = root + "/" + fname
                tweets = get_tweets(in_file)
                #print len(tweets)
                all_tweets.extend(tweets)
        #in_file = "2013_1_1"
        #tweets = get_tweets(in_file)
        count_expressions(tweets)
        count_expressions_two(tweets)

if __name__ == "__main__":
  main()

