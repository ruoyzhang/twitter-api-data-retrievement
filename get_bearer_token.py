import base64
import requests
import urllib.parse

# setting the oauthen2 path
oauth2 = 'https://api.twitter.com/oauth2/token'

def get_bearer_token(consumer_key, consumer_secret):
	"""
	function for receiving the bearer token from Twitter
	"""

	# URL encode the consumer key and the consumer secret according to RFC 1738
	# this step does not change the consumer key and secrets at the time of writing
	# however it is recommended by twitter to perform the encoding for future proofing
	consumer_key = urllib.parse.quote(consumer_key)
	consumer_secret = urllib.parse.quote(consumer_secret)

	# concatenate the above
	bearer_token = ":".join([consumer_key, consumer_secret])

	# Base64 encode the string from the previous step
	bearer_token_base64_encode = base64.b64encode(bearer_token.encode('utf-8'))

	# necessary headers for making the HTTP POST request
	headers = {"Authorization": "Basic " + bearer_token_base64_encode.decode('utf-8'),
			   "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
			   "Content-Length": "29",
			   "Accept-Encoding": "gzip",
			   }

	# now request the token
	bearer_token = requests.post(oauth2, headers = headers, data={'grant_type': 'client_credentials'})
	# convert to json format
	bearer_token = bearer_token.json()

	print('The bearer token is: {}'.format(bearer_token['access_token']))


if __name__ == "__main__":
	consumer_key = input("please enter your consumer key: ")
	consumer_secret = input("please enter your consumer secret: ")
	print('now obtaining the bearer token')
	get_bearer_token(consumer_key, consumer_secret)