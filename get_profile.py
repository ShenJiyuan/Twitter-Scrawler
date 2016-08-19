"""
    """
import sys
import tweepy
# import time
# from random import randint
# import json
import pickle

#from keys import keys #keep keys in separate file, keys.py
CONSUMER_KEY = 'YOUR CONSUMER KEY'
CONSUMER_SECRET = 'YOUR CONSUMER SECRET'
ACCESS_TOKEN = 'YOUR ACCESS TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR ACCESS TOKEN SECRET'


try:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    # api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True, parser=tweepy.parsers.JSONParser())
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
    file = sys.argv[1]
    fin = open(file,'r')
    fx = file[4:]
    
    temp = []
    t = 0
    c = 0
    for line in fin.readlines():
        if (len(line)!=0):
            temp.append(line.strip())
            t += 1
            if (t == 100):
                print ','.join(temp)
                user = api.lookup_users(user_ids=[','.join(temp)])
                print 'ok'
                fout = open('test/test_' + fx + '_' + str(c).zfill(6) + '.pkl','w')
                c += 1
                pickle.dump(user, fout)
                fout.close()
                                        
                temp = []
                t = 0
            

            # user = api.get_user(int(line)) # dict struct
            # json.dump(user,fout,indent=1)
    fin.close()
    
    print "happy"

except tweepy.TweepError:
    print "tweepy.TweepError=", tweepy.TweepError
except:
    e = sys.exc_info()[0]
    print "Error: %s" % e
#print "error."