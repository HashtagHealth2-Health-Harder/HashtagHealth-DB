import HashtagHealth_DB
import json


def load_file(file_name):
    json_file = open(file_name).read()
    tweets = json.loads(json_file)
    return tweets


def populate_data(tweet):
    Tweet_ID = tweet["tweet_id"]
    Location = tweet["geo_text"]  # AKA Tweet_Location
    DateTime = tweet["created_at"]
    Full_Tweet = tweet["text"]
    Topic = None  # not sure how to make this work yet
    Region = None  # not sure how to make this work yet
    User_ID = tweet["user_id"]
    # Twitter_Handle = tweet["user_screen_name"]

    HashtagHealth_DB.insert_tweet_main(Tweet_ID, Location, DateTime, None, Full_Tweet, None, None)
    HashtagHealth_DB.insert_tweet_tweets(Tweet_ID, Full_Tweet, Topic, DateTime, None, Location)
    HashtagHealth_DB.insert_tweet_users(User_ID, None, Region)
    HashtagHealth_DB.insert_tweet_region(None, None, Location, None)


def main():
    # this data needs to go into the database
    # we need it in main just in case
        # ID, Location, DateTime, Full_Tweet, Hashtags, Mentions
    # we need it in tweets
        # ID, Tweet_Text, Topic(foreign key), DateTime, Bio_Location, Tweet_Location
    # we need it in users
        # User_ID, Twitter_Handle, Region(foreign key)
    # we need it in all related tables
    tweets = load_file("20160930212249-782043058904920065.json")
    populate_data(tweets)

if __name__ == '__main__':
    main()
