import tweepy
from datetime import datetime
from os import environ

# Define API keys
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

# Define date for last post
file = open("last-post-day.txt", "r+")
last_post_day = int(file.read())

# Define a calendar array to print out the months by their names in Portuguese
CALENDAR = [
    '',
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro']

# Authenticate to Twitter using the defined constants
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)
now = datetime.today()

# This function is the one to be called every day to post my twitter


def tweet_college_status():
    # Only post tweet if last update was made the day before
    if (now.day != last_post_day):
        api.update_status("Julia não trancou a faculdade até o dia " +
                          str(now.day) + " de " + CALENDAR[now.month] + ".")

        print("Tweeting status...")

        # Save time to environment variable
        file.seek(0)
        file.write(str(now.day))

    else:
        print("Status was already updated today.")


tweet_college_status()

file.close()
