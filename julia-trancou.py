import tweepy
from time import sleep
from datetime import datetime
import credentials

# Define API keys
CONSUMER_KEY = credentials.CONSUMER_KEY
CONSUMER_SECRET = credentials.CONSUMER_SECRET
ACCESS_KEY = credentials.ACCESS_KEY
ACCESS_SECRET = credentials.ACCESS_SECRET

# Define time constants
SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_IN_DAY = 24

# Authenticate to Twitter using the defined constants
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)
now = datetime.today()

# This function is the one to be called every day to post my twitter


def tweet_college_status():
    api.update_status("Julia não trancou a faculdade até o dia " +
                      str(now.day + 1) + " do mês " + str(now.month) + ".")
    print("Tweeting status...")


while True:
    now = datetime.today()
    tweet_college_status()
    sleep(SECONDS_PER_MINUTE * MINUTES_PER_HOUR * HOURS_IN_DAY)
