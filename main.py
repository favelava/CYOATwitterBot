import tweepy

CONSUMER_KEY = "1Eh22nCZePf2F7LJFcG9aJiYU"
CONSUMER_SECRET = "PqATFNNf94yIHSnTbgykV3ANkWytUQJBbJ1xJtobYckOFYPQun"
ACCESS_TOKEN = "3247487138-PuOTzW3r80xYNEZxziihUbhgBEP5hSxkJ82xarK"
ACCESS_TOKEN_SECRET = "PUqU9QJovvOm17nZ1Fo9CUu85bzJDUFqt3EOZePgVomFf"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except Exception:
    print("Error during authentication")
