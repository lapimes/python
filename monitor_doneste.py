# -*- coding: utf-8 -*-
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = ''
csecret = ''
atoken = ''
asecret = ''

class listener(StreamListener):
	def on_data(self, data):
		try:
			#print data
			tweet = data.split(',"text":"')[1].split('","source')[0]
			created = data.split(',"created_at":"')[1].split('","id')[0]
			print created
			print tweet
			carpeta = os.path.abspath("/doneste")
			if not os.path.exists(carpeta):
				os.makedirs(carpeta)
			completeName = carpeta + "/doneste_%s.txt" % created
			file1 = open(completeName, "w")
			file1.write("%s ; %s ;" % (tweet, created))
			file1.close()

			return True
		except BaseException, e:
			print 'failed ondata, ', str(e)
			time.sleep(5)

	def on_error(self, status):
		print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["pizza"])
