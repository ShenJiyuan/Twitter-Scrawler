"""
    """
import sys
import tweepy
import time
from random import randint
#from requests.exceptions import Timeout, ConnectionError
#from requests.packages.urllib3.exceptions import ReadTimeoutError, ProtocolError

# keys preparations
CONSUMER_KEY = 'YOUR CONSUMER KEY'
CONSUMER_SECRET = 'YOUR CONSUMER SECRET'
ACCESS_TOKEN = 'YOUR ACCESS TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR ACCESS TOKEN SECRET'


try:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
    c = tweepy.Cursor(api.followers_ids, id = 25073877, cursor=-1) # Donald Trump
    print "type(c)=", type(c)
    print c.iterator.next_cursor
    # ===
    t = 0
    for page in c.pages():
        file = "ids_"+str(t)
        fo = open(file,"w")
        tmp = []
        # tmp.append(str(len(page))+"\n")
        for i in range(0,len(page)):
            tmp.append(str(page[i])+"\n")
        fo.writelines(tmp)
        print c.iterator.next_cursor
        print "\n"
        fo.close()
        t += 1
        if (t%15==0):
            time.sleep(200)
        print "okay"
        print "\n"
    print "done"
    # ===

#except(Timeout, ssl.SSLError, ConnectionError, ReadTimeoutError, ProtocolError) as e:
#    time.sleep(200)
#    continue
except tweepy.TweepError as e:
    #print "tweepy.TweepError="+tweepy.TweepError
    if 'Failed to send request:' in e.reason:
        print "Time out error caught"
        # time.sleep(200)
        # continue
    else:
        print "tweepy.TweepError="+tweepy.TweepError
except:
    e = sys.exc_info()[0]
    print "Error: %s" % e
#print "error."