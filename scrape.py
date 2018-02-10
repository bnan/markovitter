import base64
import requests
import json


client_key = 'V7R2H69C9kaLPiziXJFJ2o3TG'
client_secret = 'GptFtTBxTbX5QiMR4EQ99Ioq8VFMhRfgZX5lPurrXx169CO2UE'


key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')


base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
auth_resp.status_code
auth_resp.json().keys()
access_token = auth_resp.json()['access_token']

search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)    
}

search_params = {
    'screen_name': 'realDonaldTrump',
    'tweet_mode': 'extended',
    'exclude_replies': True,
    'include_rts': False,
    'count':200
	}

full_tweet_data = []

while True:


	search_url = '{}1.1/statuses/user_timeline.json'.format(base_url)

	search_resp = requests.get(search_url, headers=search_headers, params=search_params)

	tweet_data = search_resp.json()
	
	if len(tweet_data) == 0:
		break;

	full_tweet_data += tweet_data

	max_id = tweet_data[-1]['id']-1
	print(max_id)

	search_params["max_id"] = max_id



with open('trump.json', 'w') as outfile:
	json.dump(full_tweet_data, outfile)