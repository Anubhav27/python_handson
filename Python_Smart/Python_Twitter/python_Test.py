__author__ = 'Anubhav'


import python_Twitter_Constants as pyt


CONSUMER_KEY = "BABgLwyhIiOcbSW3fY3zJ6HKW"
CONSUMER_SECRET = "076LjMi2D6uhHTSYTtMyx1y9A1IbF2VEywPfiWt52ZRrfxaZEd"
ACCESS_TOKEN = "81772439-aaJSS8cKqCoOcHwVQrgdQ5ffB0IpfRGCF4bwzqNsM"
ACCESS_TOKEN_SECRET = "YoqVeo1Ug0RG05w9lKsXC9nzJDmHD6CL6WJMjDSonhPVX"

py_twt_ref = pyt.Twitter_Constants()

py_twt_ref.setConsumerKey(CONSUMER_KEY)
py_twt_ref.setConsumerSecret(CONSUMER_SECRET)
py_twt_ref.setAccessToken(ACCESS_TOKEN)
py_twt_ref.setAccessTokenSecret(ACCESS_TOKEN_SECRET)

print "consume key is : " + py_twt_ref.getConsumeKey()
#print "Consumer Key is : {}".format(py_twt_ref.getConsumeKey())
print "Consumer Secret is : {}".format(py_twt_ref.getConsumerSecret())
print "Access Token is : {}".format(py_twt_ref.getAccessToken())
print "Access Token Secret is : {}".format(py_twt_ref.getAccessTokenSecret())




