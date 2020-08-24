import tweepy

with open("Twitter API Keys.txt") as inp:
    keys = inp.read().splitlines()

CONSUMER_KEY = keys[0]
CONSUMER_SECRET = keys[1]
ACCESS_TOKEN = keys[3]
ACCESS_TOKEN_SECRET = keys[4]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except Exception:
    print("Error during authentication")
