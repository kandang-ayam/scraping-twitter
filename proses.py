import tweepy
from tweepy import OAuthHandler
import json
import os


def load_api():
    ''' Function that loads the twitter API after authorizing the user. '''

    consumer_key = 'VbR5TvRCAo5ApNdLZ24C9N6fx'
    consumer_secret = 'kwoJ7ITo29RjAy55cmqBrBMEBOMS6sAvw8QIN3dQyxRnk2338c'
    access_token = '1109444851584516096-RVYYlLMbR0ZmuUwiyyJ1J1ZpODPynL'
    access_secret = 'S6xbMN4tR2ggQ8Vx2PpVi9QQsFnNhiQb4WjlTeond1Lf5'
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    # load the twitter API via tweepy
    return tweepy.API(auth)

api = load_api()
users = ['Sinovac']


for user in users :
    name = user.split()[0]
    filename = 'tweets-'+name+'.json'
    try:
        os.remove(filename)
        read_IDs = False
    except OSError as e:
        open(filename, 'w')
        read_IDs = False
    open(filename, 'w')
    read_IDs = False
    
    if os.path.isfile(filename):
        print('Appending tweets to file named: ',filename)
        read_IDs = True
    
    if read_IDs:
        tweets = api.user_timeline(id=user, count=100)
        print('Found %d tweets' % len(tweets))
        data=[]
        create_date = ""
        text = ""
        filename = 'tweets-'+user+'.json'
        for tweet in tweets:
            datetime = tweet.created_at
            item = {"created_at": datetime.__str__(),"text":tweet.text}
            data.append(item)
        json.dump(data, open(filename, 'w'))
        # for status in tweepy.Cursor(api.user_timeline, screen_name=user, tweet_mode="extended").items():
        #     json.dump(status.full_text, open(filename, 'w'))
    else:
        print('false')

# You now have a list of tweet objects with various attributes
# check out the structure here: http://tkang.blogspot.ca/2011/01/tweepy-twitter-api-status-object.html

# For example we can get the text of each tweet
# tweets_text = [t.text for t in tweets]
# filename = 'tweets-'+user+'.json'
# json.dump(tweets_text, open(filename, 'w'))
# data=[]
# create_date = ""
# text = ""
# filename = 'tweets-'+user+'.json'
# for tweet in tweets:
#     datetime = tweet.created_at
#     item = {"created_at": datetime.__str__(),"text":tweet.text}
#     data.append(item)

# json.dump(data, open(filename, 'w'))
# print('Saved to file:', filename)

# Can load file like this
#tweets_text = json.load(open(filename, 'r'))
