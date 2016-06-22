__author__ = 'Anubhav'

class Twitter_Constants:
    CONSUMER_KEY = ""
    CONSUMER_SECRET = ""
    ACCESS_TOKEN = ""
    ACCESS_TOKEN_SECRET = ""

    def __init__(self,CONSUMER_KEY = "",CONSUMER_SECRET="",ACCESS_TOKEN="",ACCESS_TOKEN_SECRET=""):
        self.CONSUMER_KEY = CONSUMER_KEY
        self.CONSUMER_SECRET = CONSUMER_SECRET
        self.ACCESS_TOKEN = ACCESS_TOKEN
        self.ACCESS_TOKEN_SECRET = ACCESS_TOKEN_SECRET

    def getConsumeKey(self):
        return self.CONSUMER_KEY

    def setConsumerKey(self,CONSUMER_KEY):
        self.CONSUMER_KEY = CONSUMER_KEY

    def getConsumerSecret(self):
        return self.CONSUMER_SECRET

    def setConsumerSecret(self,CONSUMER_SECRET):
        self.CONSUMER_SECRET = CONSUMER_SECRET

    def getAccessToken(self):
        return self.ACCESS_TOKEN

    def setAccessToken(self,ACCESS_TOKEN):
        self.ACCESS_TOKEN = ACCESS_TOKEN

    def getAccessTokenSecret(self):
        return self.ACCESS_TOKEN_SECRET

    def setAccessTokenSecret(self,ACCESS_TOKEN_SECRET):
        self.ACCESS_TOKEN_SECRET = ACCESS_TOKEN_SECRET






