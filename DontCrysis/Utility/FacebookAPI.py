import facebook
import urllib2
import requests
import urllib
import urlparse
import subprocess
__author__ = 'Madhavan'
#def main():
#  message = "This is a test Post from Thunder Groudon 1323"
#  FacebookAPI(message)

def FacebookAPI(message):
    app_id = ""
    scope = "publish_pages,manage_pages"
    app_secret = ""

    access_token = "CAACNkNvwkZC4BAKgsT7Ski27g6tJbCRpFrc0h2lvDQDmLWtTb30iH4YuXo09Iv1sFUesSACKv0gUZCZAmGHWRNIZBfJfWDjaIUUeAbYDo4kA6atQbZBp3jVeRJsfg16CCZBV2u8gF9aQRWJUeuSFefAZCiYxY9yY514DldQQD1o9i8DJzMMg9iE2Ank1WDbXCAZD"
    app_id = "155653304783870"                       # Obtained from https://developers.facebook.com/
    client_secret = "20f17d664ab5cb946334ac33a8db3ea6"         # Obtained from https://developers.facebook.com/

    #payload = {'grant_type': 'fb_exchange_token','fb_exchange_token':access_token, 'client_id': app_id, 'client_secret': client_secret}
    #response = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
    #print response.text
    #access_token = response.text.split('=')[1]
    #print access_token
    cfg = {
    "page_id"      : "428266620709236",  # Step 1
    "access_token" : access_token
    }

    api = get_api(cfg)
    msg = message
    status = api.put_wall_post(msg)
    return

def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  #print cfg['access_token']
  resp = graph.request('me/accounts')
  page_access_token = None
  #print resp
  for page in resp['data']:
        print page
        if page['id'] == cfg['page_id']:
            page_access_token = page['access_token']
            print page_access_token
  #print page_access_token
  graph = facebook.GraphAPI(page_access_token)
  return graph

#if __name__ == "__main__":
#  main()
