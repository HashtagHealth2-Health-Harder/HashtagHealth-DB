import HashtagHealth_DB
import json 
result = HashtagHealth_DB.get_latest_tweet()
print(result.fetchone())