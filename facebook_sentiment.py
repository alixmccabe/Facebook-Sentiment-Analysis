"""Hey, your organization makes it really hard for me to figure out what your project is.
I first checked "Facebook_Sentiment_Analysis inside your comp_art repo, and it was empty.
I then found facebook_sentiment files inside your comp_art repo, which was old, and I almost graded that.
I finally found this and your write up though, so you had everything - it was just hard to find.
Plese help yourself and me by cleaning your github repos and folder organizations.

It would also be really helpful to label your figures in the code itself, though I see it is there
in the write up.

+Functionality: 5/5
+Documentation: 4/5 (You might consider letting the users know to run import_friends first before running main in 
	order to pickle the file first. Or even better, create a seperate main function for "first_run")
+Style: 4/5 (Check if you're making your code unessarily hard to read, as I explained in your last function.
	Also clean up your githup folder organization, and get get rid of random files like 
	"yelp_goofing" and empty files like "text_mining" or the empty folder "Facebook-Sentiment-Analysis)
+CheckIn: yes
+Total: 4.25/5"""

"""This program imports my friends' statuses from facebook and 
groups them via MDS according to Pattern's sentiment axis"""
from pattern.web import *
from pattern.en import *
from pylab import *
import pickle
import string


def import_friends():
	"""this function pickles the latest newsfeed from my facebook page

	r.text: a status or news update
	r.author: the host or author of the facebook status
	text_author_pickle: the name of the file that saves my newsfeed
	"""
	f = Facebook(license='CAAEuAis8fUgBACpOVZA8pT2YecghBKjGPNRIQka7CH0CZCSzkkAt1kYvgZBta6rtJhUfWBAx5QZCh4IiPaDazbK5WfLZBI6lkaduhxKyXHJzhRszPRwOKv47KZBrodtpGVvzfwdxBLsenWsTLtaw6LyfyxeVXKNqLZAlmz3ZCqpwvlI4drTrNZBVH')
	me = f.profile()

	my_friends = f.search(me[0], type=FRIENDS, count=10000)
	
	for user in my_friends:
		for r in f.search(user.id, type=NEWS, count=100):
			
			post_friend += (r.text,r.author)

		#save pickled data for later use
		p = open('text_author.pickle','w')
		pickle.dump((post_friend),p)
		p.close()

def sentiment_gage():
	"""this function analyzes how subjective and positive each friend's stati are based on pattern's sentiment function
	returns average sentiment of each friend

	Because there's so much excess information in the pickled file, it's necessary to track only status's of my friends
	we can do this by tracking only elements of text_author.pickle with sentiment[0:1] != [0.0]
	
	sent: a list we process to return only statuses
	"""
	f = open("text_author.pickle",'r')
	lines_in_text = f.readlines()

	#a list of statuses 
	sent = []

	#eliminating punctuation for ease of processing
	for i in range(len(lines_in_text)):
		lines_in_text[i] = lines_in_text[i].translate(string.maketrans("",""), string.punctuation)

	#storing statuses in a returnable, plottable format
	for line in lines_in_text:
		if sentiment(line)[0] != 0.0 and sentiment(line)[1] != 0.0:
			sent += sentiment(line)
	return sent

	#Allright, what makes more sense to me, is instead of returning a giant list of sentiment values all jumbled together,
	# to rather return a list of tuples, where each tuple represents a status, and is (positivity, objectivity) 
	# Organizing it that way will make more sense to readers, and will allow you to then loop 
	# through the data in a more clear way

def sentiment_map():
	"""
	this function maps each status based on its sentiment value in an x-y plane

	sentiment: the returned list of statuses from our sentiment_gage() function
	"""
	sentiment = sentiment_gage()
	
	#creating a plot for objectivity and negativity
	i = 1
	while i < len(sentiment):
		plot(sentiment[i-1],sentiment[i],'o')
		i += 1
	show()
	
	#Oooh, this is really messy to a reader. Check my comment in the above function on instead organizing
	# sentiment as a list of tuples. This would really allow you to simplify this loop by just doing:

	# for status in sentiment:
	# 	plot(sentiment[0], sentiment[1], 'o')

if __name__=="__main__":
	sentiment_map()