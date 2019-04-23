import tweepy
import os
import time
print('this is my twitter bot')
CONSUMER_KEY = 'zRJb9ldoYKWwSx6PEf9gtzZa7' 
CONSUMER_SECRET ='Q87Uk09TnqPHyhmW5C27YSHc0h7A5kqX5cjCSXNK2TEm02jgVA'
ACCESS_KEY = '1119825600154234880-kSkToton1DoWJLmMZEJg8MiYdwL3sH'
ACCESS_SECRET = 'AH18wLIGmAB5kMcXAE26DyceMHQeCly0NqFz2l7xktMlX'
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)


FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    print('replying to tweets')
    f_read = open(file_name,'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name,'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    #if os.path.isfile(/last_seen_id.txt) and os.path.getsize(/last_seen_id.txt) > 0
    #6th tweet id 1119847802513674242
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
                            last_seen_id,
                            tweet_mode='extended')



    for mention in reversed(mentions):
        print(str(mention.id) + '-' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#helloworld' in mention.full_text.lower():
            print('Found hello world')
            print('responding back....')
            api.update_status('@' + mention.user.screen_name + '#HelloWorld back to you! ', mention.id)

while True:
    reply_to_tweets()
    time.sleep(2)