
#nltk functions
import nltk

#gensim, library to make topic modelling
from gensim import models, corpora

#python utilities
import re
import json
from itertools import chain


###
# III iteration of my learning of topic modelling [OK]
# desc.: tokenization, stopword removal, LDA, word frecuency.

#number of topics to look for
NUM_TOPICS = 10

#get stop_words from nltk
stop_words = nltk.corpus.stopwords.words('english')
#add stop_words that belongs to the context
exclude = ['elixir','software','use','web','development','phoenix']
stop_words.extend(exclude)

#clean_text() could be modified to fit nature of dataset
#input must be a string (a line, a paragraph,...)
def clean_text(text):		
	text = text.replace('-',' ')
	text = text.replace('/',' ')
	text = text.lower()	
	tokenized_text = nltk.word_tokenize(text) # list of strings
	cleaned_text   = [t for t in tokenized_text 
											if t.lower() not in stop_words
											and re.match('[a-zA-Z\-][a-zA-Z\-]{2,}',t)]

	return cleaned_text

#getting my data from json file
#this data contains description about a set of companies using certain technology
file_path = '../scraped_data/elixir_companies.json'
with open(file_path) as f:
	data = json.load(f)

##For genism we nee to tokenize data and filter out stopwords
#list of descriptions of companies
description_list = [company['description'] for company in data]
tokenized_data   = [clean_text(text) for text in description_list] #list of lists
#print(tokenized_data[0])

#Build a dictionary - associate word to numeric id
dictionary = corpora.Dictionary(tokenized_data)

#Transform collection of text to numerical form
corpus = [dictionary.doc2bow(text) for text in tokenized_data]

#Build the LDA model
lda_model = models.LdaModel(corpus = corpus, num_topics = NUM_TOPICS, id2word = dictionary)

print("LDA model: ")
for idx in range(NUM_TOPICS):
	#print("Topic #%s" % idx, lda_model.print_topic(idx,10))	
	#print("Topic #%s" % idx, lda_model.show_topic(idx,10))
	topic_summary = ' '.join([ v[0] for v in lda_model.show_topic(idx,10) ])
	print("Topic #%s : %s " % (idx, topic_summary))
		
print("=" * 20)

##Checking out word frequency
#list of all the words in the documents
word_set = list(chain.from_iterable(tokenized_data))
fdist = nltk.FreqDist(word_set)

print("total of words: %d " % len(word_set))
print("Word Freq distribution: ")
for w,f in fdist.most_common(10):
	print('{};{}'.format(w,f))


