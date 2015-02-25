"""This program imports my friends' statuses from facebook and 
groups them via MDS according to Pattern's sentiment axis"""
from pattern.web import *
from pattern.en import *
from pylab import *
import pickle
import string
#from buzz_words import index, words, buzz_words


def import_friends():
	"""this function pickles the latest newsfeed from my facebook page

	post_friend: A list of post's from my newsfeed in conjuction with the friend that posted it
	text_author_pickle: the name of the file that saves my newsfeed
	"""
	f = Facebook(license='CAAEuAis8fUgBACpOVZA8pT2YecghBKjGPNRIQka7CH0CZCSzkkAt1kYvgZBta6rtJhUfWBAx5QZCh4IiPaDazbK5WfLZBI6lkaduhxKyXHJzhRszPRwOKv47KZBrodtpGVvzfwdxBLsenWsTLtaw6LyfyxeVXKNqLZAlmz3ZCqpwvlI4drTrNZBVH')
	me = f.profile()

	my_friends = f.search(me[0], type=FRIENDS, count=10000)
		
	post_friend = []
	
	for user in my_friends:
		for r in f.search(user.id, type=NEWS, count=100):
			
			post_friend += (r.text,r.author)

		#save to a file so that we can load file later
		p = open('text_author.pickle','w')
		pickle.dump((post_friend),p)
		p.close()

def sentiment_gage():
	"""this function analyzes how subjective and positive each friend's stati are based on pattern's sentiment function
	returns average sentiment of each friend

	Because there's so much excess information in the pickled file, it's necessary to track only status's of my friends
	we can do this by tracking only elements of text_author.pickle with sentiment[0:1] != [0.0]
	"""
	f = open("text_author.pickle",'r')
	lines_in_text = f.readlines()

	sent = []

	for i in range(len(lines_in_text)):
		lines_in_text[i] = lines_in_text[i].translate(string.maketrans("",""), string.punctuation)


	for line in lines_in_text:
		if sentiment(line)[0] != 0.0 and sentiment(line)[1] != 0.0:
			sent += sentiment(line)
	return sent


def sentiment_map():
	"""
	this function maps each status based on its sentiment value 
	"""
	sentiment = sentiment_gage()
	
	i = 1
	while i < len(sentiment):
		plot(sentiment[i-1],sentiment[i],'o')
		i += 1
	show()

sentiment_map()