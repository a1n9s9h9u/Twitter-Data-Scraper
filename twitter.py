import tweepy
import pandas as pd 
import json
from datetime import datetime

class TwitterDataScraper:

    def get_and_save_tweets(self, user_name, count):

        access_key = "XXXX"
        access_secret = "XXXX"
        consumer_key = "XXXX"
        consumer_secret = "XXXX"

        auth = tweepy.OAuthHandler(access_key, access_secret)
        auth.set_access_token(consumer_key, consumer_secret)
        api = tweepy.API(auth)

        tweets = api.user_timeline(screen_name=user_name, 
            count=count, include_rts = False, tweet_mode = 'extended')

        tweets_list = []

        for tweet in tweets:

            text = tweet._json["full_text"]

            structured_tweet = {

                "user": tweet.user.screen_name, 
                'text' : text, 
                'favorite_count' : tweet.favorite_count, 
                'retweet_count' : tweet.retweet_count, 
                'created_at' : tweet.created_at

                }

            tweets_list.append(structured_tweet)
    
        df = pd.DataFrame(tweets_list)
        df.to_csv('twitter.csv')


if __name__ == "__main__":

    obj_twitter_data_scraper = TwitterDataScraper()

    obj_twitter_data_scraper.get_and_save_tweets('@elonmusk', 100)
