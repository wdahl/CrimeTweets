# William Dahl
# 001273655
# ICSI 431 - Data Mining

import tweepy, sys

reload(sys)
sys.setdefaultencoding("utf-8")

OAuth = tweepy.OAuthHandler('PeH7lROp4ihy4QyK87FZg', '1BdUkBd9cQK6JcJPll7CkDPbfWEiOyBqqL2KKwT3Og')
OAuth.set_access_token('1683902912-j3558MXwXJ3uHIuZw8eRfolbEGrzN1zQO6UThc7', 'e286LQQTtkPhzmsEMnq679m7seqH4ofTDqeArDEgtXw')
myApi = tweepy.API(OAuth)

def query1():
	geo = "38.9072,-77.0369,68.34mi"
	query = "crime AND Washington DC"
	tweets = myApi.search(q=query, geocode=geo)
	f = open("query1.txt", "w")
	for tweet in tweets:
		f.write(str(tweet.created_at))
		f.write(", " + tweet.user.screen_name + ", " + tweet.text + "\n")
		f.write("*******************************************************\n")

def query2():
	geo = "38.9072,-77.0369,68.34mi"
	query = "police AND Washington DC"
	tweets = myApi.search(q=query, geocode=geo)
	f = open("query2.txt", "w")
	for tweet in tweets:
		f.write(str(tweet.created_at))
		f.write(", " + tweet.user.screen_name + ", " + tweet.text + "\n")
		f.write("*******************************************************\n")

def query3():
	geo = "38.9072,-77.0369,68.34mi"
	query = "theft AND Washington DC"
	tweets = myApi.search(q=query, geocode=geo)
	f = open("query3.txt", "w")
	for tweet in tweets:
		f.write(str(tweet.created_at))
		f.write(", " + tweet.user.screen_name + ", " + tweet.text + "\n")
		f.write("*******************************************************\n")

def query4():
	geo = "38.9072,-77.0369,68.34mi"
	query = "stolen AND Washington DC"
	tweets = myApi.search(q=query, geocode=geo)
	f = open("query4.txt", "w")
	for tweet in tweets:
		f.write(str(tweet.created_at))
		f.write(", " + tweet.user.screen_name + ", " + tweet.text + "\n")
		f.write("*******************************************************\n")

def query5():
	geo = "38.9072,-77.0369,68.34mi"
	query = "murder AND Washington DC"
	tweets = myApi.search(q=query, geocode=geo)
	f = open("query5.txt", "w")
	for tweet in tweets:
		f.write(str(tweet.created_at))
		f.write(", " + tweet.user.screen_name + ", " + tweet.text + "\n")
		f.write("*******************************************************\n")

def random_data():
	geo = "38.9072,-77.0369,68.34mi"
	tweets = myApi.search(geocode=geo, count=100)
	f = open("random_data.txt", "w")
	for tweet in tweets:
		f.write(str(tweet.created_at))
		f.write(", " + tweet.user.screen_name + ", " + tweet.text + "\n")
		f.write("*******************************************************\n")

if __name__ == '__main__':
	query1()
	query2()
	query3()
	query4()
	query5()
	random_data()