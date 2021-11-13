import tweepy
from datetime import datetime
from os import environ

# Define API keys
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

# Set id for my personal account
PERSONAL_ID = environ['PERSONAL_ID']
dropped_out = False

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

# Create messages object
messages = api.get_direct_messages()

# This function is the one to be called every day to post my twitter


def tweet_college_status():
    # Only post tweet if last update was made the day before
    if (now.day != last_post_day):
        if dropped_out == False:
            api.update_status("Julia não trancou a faculdade até o dia " +
                              str(now.day) + " de " + CALENDAR[now.month] + ".")

        if dropped_out == True:
            api.update_status("Julia trancou a faculdade.")

        print("Tweeting status...")

        # Save time to environment variable
        file.seek(0)
        file.write(str(now.day))

    else:
        print("Status was already updated today.")


for message in messages:
    # Check if message was sent by my personal account
    if message.message_create['sender_id'] == PERSONAL_ID:
        # Check if the answer "yes" was given from my personal account
        if message.message_create['message_data']['text'] == "yes" or message.message_create['message_data']['text'] == "y":
            dropped_out = True
            tweet_college_status()
            break

        tweet_college_status()
        break

file.close()
