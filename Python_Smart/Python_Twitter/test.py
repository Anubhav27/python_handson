__author__ = 'Anubhav'

reqURL = "https://api.twitter.com/1.1/statuses/user_timeline.json"


import base64
import random
import urllib
import ConfigParser
import time
import collections
import requests
#this function will do base encoding of string in the rang 0 to 9
def base64en():
    encoded_string = base64.b64encode(''.join([str(random.randint(0, 9)) for i in range(24)]))

    return encoded_string

#this function will return encoded url
def escape(s):
    return urllib.quote(s,safe='~')


def get_nonce():
    """Unique token generated for each request"""
    n = base64.b64encode(
        ''.join([str(random.randint(0, 9)) for i in range(24)]))
    return n


def get_oauth_parameters(consumer_key, access_token):
    """Returns OAuth parameters needed for making request"""
    oauth_parameters = {
        'oauth_version': "1.0",
        'oauth_signature_method': "HMAC-SHA1",
        'oauth_nonce': get_nonce(),
        'oauth_timestamp': str(int(time.time())),
        'oauth_consumer_key': consumer_key,
        'oauth_token': access_token


    }

    return oauth_parameters


def create_auth_header(parameters):
    """For all collected parameters, order them and create auth header"""
    ordered_parameters = {}
    ordered_parameters = collections.OrderedDict(sorted(parameters.items()))
    auth_header = (
        '%s="%s"' % (k, v) for k, v in ordered_parameters.iteritems())
    val = "OAuth " + ', '.join(auth_header)
    return val


#print escape(reqURL)


method="get"
url = reqURL


config = ConfigParser.RawConfigParser()
config.read('settings.cfg')

#configuration hash for the keys
keys = {
    "twitter_consumer_secret": config.get('Keys', 'CONSUMER_SECRET'),
    "twitter_consumer_key": config.get('Keys', 'CONSUMER_KEY'),
    "access_token": config.get('Keys', 'ACCESS_TOKEN'),
    "access_token_secret": config.get('Keys', 'ACCESS_TOKEN_SECRET')
}

oauth_parameters = get_oauth_parameters(
        keys['twitter_consumer_key'],
        keys['access_token']
    )




print oauth_parameters


oauth_parameters['oauth_signature'] = "T4zCtxOdtLO%2FTiZ0u5xyW9t74Yo%3D"

headers = {'Authorization': create_auth_header(oauth_parameters)}

print headers

r = requests.get(url, headers=headers)

print r.json()



