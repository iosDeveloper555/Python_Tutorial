import tweepy as tw
import pandas as pd
# intialize the dataframe
search_query = "#covid19"
auth = tw.OAuthHandler('oMyMYy7EZhICWy7WFVyCTeJgc','cwXtjZFaJ7D15CJfly77HS3pe9ync2DoaZEOHaXvM5I3kJvsHH')
auth.set_access_token('2170300532-LmY24IinU6Enj252r4TKGxiZzD851ERp1P2RUkX','BtPiXMjmCR8mPlH1DexuKQuNK0lmHWhNJaTGM6750En68')
api = tw.API(auth)

tweets_df = pd.DataFrame()
# get tweets from the API
tweets = tw.Cursor(api.search_tweets,
                   q=search_query).items(10)

# store the API responses in a list
tweets_copy = []
for tweet in tweets:
   print(tweet.user.name)
   print(tweet.user.location)

   tweets_copy.append(tweet)

print("Total Tweets fetched:", len(tweets_copy))

# populate the dataframe
for tweet in tweets_copy:
    hashtags = []
    try:
        for hashtag in tweet.entities["hashtags"]:
            hashtags.append(hashtag["text"])
        text = api.get_status(id=tweet.id, tweet_mode='extended').full_text
    except:
        pass
    tweets_df = tweets_df.append(pd.DataFrame({'user_name': tweet.user.name,
                                               'user_location': tweet.user.location,\
                                               'user_description': tweet.user.description,
                                               'user_verified': tweet.user.verified,
                                               'date': tweet.created_at,
                                               'text': text,
                                               'hashtags': [hashtags if hashtags else None],
                                               'source': tweet.source}))
    tweets_df = tweets_df.reset_index(drop=True)

# show the dataframe
tweets_df.head()

''' 

import tweepy
import pandas as pd


auth = tweepy.OAuthHandler('oMyMYy7EZhICWy7WFVyCTeJgc','cwXtjZFaJ7D15CJfly77HS3pe9ync2DoaZEOHaXvM5I3kJvsHH')
auth.set_access_token('2170300532-LmY24IinU6Enj252r4TKGxiZzD851ERp1P2RUkX','BtPiXMjmCR8mPlH1DexuKQuNK0lmHWhNJaTGM6750En68')

api = tweepy.API(auth)
user = api.get_user(screen_name='twitter')

print(user.screen_name)
print("user.followers_count = ", user.followers_count)
print("user.friends = ", user.friends)

for friend in user.friends():
   print(friend.screen_name)

'''  # Get home time line
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
    
    '''
    
    '''
