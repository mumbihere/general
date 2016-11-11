import urllib.request
from urllib.parse import *
import json
import oauth2
import settings as SETTINGS
'''
Citations
http://stackoverflow.com/questions/606191/convert-bytes-to-a-python-string
https://docs.python.org/3.0/howto/urllib2.html
https://www.yelp.com/developers/api_console

'''


# Please assign following values with the credentials found in your Yelp account, 
# you can find them here: http://www.yelp.com/developers/manage_api_keys 
CONSUMER_KEY = SETTINGS.CONSUMER_KEY
CONSUMER_SECRET = SETTINGS.CONSUMER_SECRET 
TOKEN = SETTINGS.TOKEN 
TOKEN_SECRET =SETTINGS.TOKEN_SECRET

# yelp_req() function description:
# The input is a url link, which you use to make request to Yelp API, and the 
# return of this function is a JSON object or error messages, including the information 
# returned from Yelp API.
# For example, when url is 'http://api.yelp.com/v2/search?term=food&location=San+Francisco'
# yelp_req(url) will return a JSON object from the Search API

def yelp_req(url):
    """ Pass in a url that follows the format of Yelp API,
        and this function will return either a JSON object or error messages.
    """
    oauth_request = oauth2.Request('GET', url, {})
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
    response = None

    #conn = urllib.urlopen(signed_url, None)
    try:
        conn = urllib.request.urlopen(signed_url, None) #https://docs.python.org/3.0/howto/urllib2.html
        try:
            #response = json.loads(conn.read())
            response = json.loads(conn.read().decode("utf-8")) #http://stackoverflow.com/questions/606191/convert-bytes-to-a-python-string
        finally:
            conn.close()
    except:
        pass
    return response

#################################################################################
# Your code goes here
offset = 0
file = open('restaurants2.monicah.wambugu.txt', 'w',encoding='utf-8')
for offset in range(2):
    start = offset*20
    params = urllib.parse.urlencode({
        'location':'San Francisco, CA',
        'category_filter':'restaurants',
        #'term':'restaurants',
        'sort':'2',
        'limit':'20',
        'offset':start
        })
    url = 'https://api.yelp.com/v2/search/?%s' % params

    api_results = yelp_req(url)
    if api_results:
        restaurants = api_results['businesses']
        for r in restaurants:
            restraunt_entry = str(r['name'])+','+str(r['review_count'])+'\n'
            file.write(restraunt_entry)
    else:
        print('There was an error accessing the API')
file.close()           


