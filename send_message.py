import tweepy
from os import environ

# Define API keys
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

PERSONAL_ID = environ['PERSONAL_ID']
dropped_out = False

# Authenticate to Twitter using the defined constants
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# Set API object
api = tweepy.API(auth)


# Create messages object
messages = api.get_direct_messages()

for message in messages:

    # Check if message was sent by my personal account
    if message.message_create['sender_id'] == PERSONAL_ID:

        # Check if the answer "yes" was given from my personal account
        if message.message_create['message_data']['text'] == "yes" or message.message_create['message_data']['text'] == "y":
            dropped_out = True
            print("Dropped out.")
            break

        break

if (dropped_out != True):
    api.send_direct_message(PERSONAL_ID, "Did you drop out?")
