import HashtagHealth_DB
import pickle


def load_file(file_name):
    tweets = pickle.load(open(file_name, 'rb'))
    return tweets


def populate_data(tweet):
    Tweet_ID = tweet.id
    Location = tweet.place.full_name  # AKA Tweet_Location
    DateTime = tweet.created_at
    Full_Tweet = tweet.extended_tweet["full_text"]
    Hashtags = tweet.entities["hashtags"]
    Mentions = tweet.entities["user_mentions"]
    Topic = None  # not sure how to make this work yet
    Region = None  # not sure how to make this work yet
    Bio_Location = tweet.user.location  # AKA Profile_location
    User_ID = tweet.user.id
    Twitter_Handle = tweet.user.screen_name
    Exact_Location = tweet.coordinates
    Country = tweet.place.country_code
    City = tweet.place.name

    HashtagHealth_DB.insert_tweet_main(Tweet_ID, Location, DateTime, Bio_Location, Full_Tweet, Hashtags, Mentions)
    HashtagHealth_DB.insert_tweet_tweets(Tweet_ID, Full_Tweet, Topic, DateTime, Bio_Location, Location)
    HashtagHealth_DB.insert_tweet_users(User_ID, Twitter_Handle, Region)
    HashtagHealth_DB.insert_tweet_region(Exact_Location, Country, Location, City)


def main():
    # this data needs to go into the database
    # we need it in main just in case
        # ID, Location, DateTime, Full_Tweet, Hashtags, Mentions
    # we need it in tweets
        # ID, Tweet_Text, Topic(foreign key), DateTime, Bio_Location, Tweet_Location
    # we need it in users
        # User_ID, Twitter_Handle, Region(foreign key)
    # we need it in all related tables
    tweets = load_file("2017-06-16_2004081497643448938.pickle")
    populate_data(tweets)
    print("Table created?")

if __name__ == '__main__':
    main()
