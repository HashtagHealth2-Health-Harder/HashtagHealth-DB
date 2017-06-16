import HashtagHealth_DB
import tweepy
import pickle


def load_file (file_name, array):
    # try:
        # tweet = pickle.load(open(file_name))
    with open(file_name, 'rb') as file:
        a = pickle.load(file)
        print(a)
    return array
    # except:
    #    print("Could not unpickle file")

def main():
    # this data needs to go into the database
    # we need it in main just in case
    # we need it in tweets
    # we need it in users
    # we need it in all related tables

    tweets = ["bob", 3, "hello world"]
    tweets = load_file("2017-06-16_2004081497643448938.pickle", tweets)
    # for i in tweets:
    #    print(i)



if __name__ == '__main__':
    main()