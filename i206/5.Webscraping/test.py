import requests
import oauth2
import json

CONSUMER_KEY = 'lQmlC0AgF_7kn7cxHP8ZTg'
CONSUMER_SECRET = 'SyTV8vvUefKgH_3U32Xz2bxGeMk'
TOKEN = 'mVJTyhoM-F-TYWyLbTaiJXE1JcTSiAP2'
TOKEN_SECRET = 'fyuOu_bNyrkkD-jQpoPPzhyWBR0'


def requestData(location):
    '''
    Authenticates a request and returns
    data from Yelp API.
    '''
    data = []
    url = 'https://api.yelp.com/v2/search/?location=San Francisco, CA'

    oauth_request = oauth2.Request(method="GET", url=url)

    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': TOKEN,
            'oauth_consumer_key': CONSUMER_KEY
        }
    )
    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    token = oauth2.Token(TOKEN, TOKEN_SECRET)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()
    req = requests.get(signed_url)
    response = req.text

    return response

print(requestData('43'))
