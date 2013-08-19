import simplejson as json
import sys, os
import urllib, urllib2, base64

username = "#Enter your username"
password = "#Enter your password"

api_base="https://api.catch.com/v3/"

def get(path):
	request = urllib2.Request(api_base+path)
	base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
	request.add_header("Authorization", "Basic %s" % base64string)   
	response = json.loads(urllib2.urlopen(request).read())['result']

	return response