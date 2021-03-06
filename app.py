#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests,flask,requests_oauthlib

app = flask.Flask(__name__)

oauth_token = "" # Your OAuth Token
oauth_token_secret "" # Your OAuth Token secret

##########
# Twitter Official keys : https://gist.github.com/shobotch/5160017
# API : http://seriot.ch/resources/abusing_twitter_api/twitter_api.pdf
# http://spotidoc.com/doc/715113/visual-documentation-of-twitter-api
# Nicolas Seriot @ Project Manager ST Twitter .
tweets = lambda username: requests.get('https://api.twitter.com/2/timeline/profile/'+requests.get('https://help.twitter.com/api/v1/username_lookups?username='+username).json()['user_id']+'.json?count=32767&include_tweet_replies=false&pc=true&earned=true&autoplay_enabled=true&include_entities=true&include_cards=true&cards_platform=Android-12&include_carousels=true&ext=stickerInfo%2CmediaRestrictions%2CaltText%2CmediaStats%2CmediaColor%2Cinfo360%2CcameraMoment%2Cmaster_playlist_only&include_media_features=true&include_blocking=true&include_blocked_by=true&tweet_mode=extended&include_reply_count=true&include_composer_source=true&simple_quoted_tweet=true&include_ext_media_availability=true&include_user_entities=true&include_profile_interstitial_type=true',auth=requests_oauthlib.OAuth1('3nVuSoBZnx6U4vzUxf5w','Bcs59EFbbsdF6Sl9Ng71smgStWEGwXXKSjYvPVt7qys',oauth_token,oauth_token_secret,decoding=None)).text

@app.route('/')
def index():
    return flask.Response('{"endpoint":[{"Method":"GET","Params":"/<username-twitter>","Test":"https://all-tweets.herokuapp.com/0x1337r00t"}],"Project":"https://github.com/1337r00t/ALL-Tweets"}',status=200,mimetype='application/json')

@app.route('/<username>',methods=['GET'])
def check(username):
    return flask.Response(tweets(username),status=200,mimetype='application/json')
    
if __name__ == "__main__":
    app.run()
