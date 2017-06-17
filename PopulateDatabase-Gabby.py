import HashtagHealth_DB
import pickle


def load_file(file_name):
    tweets = pickle.load(open(file_name, 'rb'))
    return tweets


def main():
    # this data needs to go into the database
    # we need it in main just in case
    # we need it in tweets
    # we need it in users
    # we need it in all related tables
    tweets = load_file("2017-06-16_2004081497643448938.pickle")
    #print(tweets.id)
    #print(tweets.place.full_name)
    #print(tweets.created_at)
    #print(tweets.user.location)
    #print(tweets.extended_tweet["full_text"])
    #print(tweets.entities["hashtags"])
    #print(tweets.entities["user_mentions"])
    HashtagHealth_DB.insert_tweet(tweets.id, tweets.place.full_name, tweets.created_at, tweets.user.location,
                                  tweets.extended_tweet["full_text"], tweets.entities["hashtags"],
                                  tweets.entities["user_mentions"])
    print("Table created?")

if __name__ == '__main__':
    main()
