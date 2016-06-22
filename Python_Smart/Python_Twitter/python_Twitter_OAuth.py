#client request access to request based on behalf of user
"""
def genConsumerKey():
    return

def genConsumerSecret():
    return

def genOAuthVersion():
    return

def genOAuthNoOnce():
    return

def genOAuthTimeStamp():
    return

def genOAuthSigMethod():
    return

def genOAuthToken():
    return

def genOAuthSignature():
    return

"""

import urllib
from oauth import oauth
import oauthlib
import requests_oauthlib

Consumer_Key = "BABgLwyhIiOcbSW3fY3zJ6HKW"
Consumer_Secret = "076LjMi2D6uhHTSYTtMyx1y9A1IbF2VEywPfiWt52ZRrfxaZEd"
Access_Token = "81772439-aaJSS8cKqCoOcHwVQrgdQ5ffB0IpfRGCF4bwzqNsM"
Access_Token_Secret = "YoqVeo1Ug0RG05w9lKsXC9nzJDmHD6CL6WJMjDSonhPVX"
App_only_authentication = "https://api.twitter.com/oauth2/token"
Request_token_URL = "https://api.twitter.com/oauth/request_token"
Authorize_URL = "https://api.twitter.com/oauth/authorize"
Access_token_URL = "https://api.twitter.com/oauth/access_token"

credentials = {"CONSUMER_KEY" : Consumer_Key,
        "CONSUMER_SECRET" : Consumer_Secret
        }


twitter = requests_oauthlib.OAuth1Session(client_key=Consumer_Key,
                            client_secret=Consumer_Secret,
                            resource_owner_key=Access_Token,
                            resource_owner_secret=Access_Token_Secret)

url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

r = twitter.get(url)

print r.json()



