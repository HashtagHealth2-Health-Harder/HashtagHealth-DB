import HashtagHealth_DB
import exceptions
import pickle


def load_file(file_path, file_name):
    try:
        tweets = []
        from file_path import file_name
        with open(file_name) as f:
            for line in f:
                tweets.append(pickle.decode_long(line))
        return tweets
    except exceptions as e:
        print(e)

def main():
    # this data needs to go into the database
    # we need it in main just in case
    # we need it in tweets
    # we need it in users
    # we need it in all related tables
