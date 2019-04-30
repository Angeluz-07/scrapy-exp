
#nltk functions
import nltk

#gensim, library to make topic modelling
from gensim import models, corpora
from gensim.parsing.porter import PorterStemmer

#python utilities
import re
import json
from itertools import chain

###
# IV iteration of my learning of topic modelling
# desc.: tokenization, stopword removal, LDA, word frecuency, stemmer, lemmatizer.s


#number of topics to look for
NUM_TOPICS = 10

#get stop_words from nltk
stop_words = nltk.corpus.stopwords.words('english')
#add stop_words that belongs to the context
exclude = [
						'elixir','software','use','web','development','phoenix','product',
						'based','company','http','build','using','application','backend',
						'business','solution','technology','amp','system','make','github.com',
						'building','usa','project','help','provides','provide','also','apps',
						'open','source','used','real','time','service','mobile'
					]
stop_words.extend(exclude)

#stemmer
ps = nltk.stem.PorterStemmer()
#lemmatizer
wl = nltk.stem.WordNetLemmatizer()

#clean_text() could be modified to fit nature of dataset
#input must be a string (a line, a paragraph,...)
def clean_text(text):		
	text = text.replace('-',' ')
	text = text.replace('/',' ')
	text = text.lower()	
	tokenized_text = nltk.word_tokenize(text) # list of strings	
	tokenized_text = [wl.lemmatize(w) for w in tokenized_text]
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

##Remove words with just one ocurrence
#list of all the words in the documents
word_set = list(chain.from_iterable(tokenized_data))
fdist = nltk.FreqDist(word_set)
low_freq_words = [ w[0] for w in list(filter(lambda x: x[1]==1, fdist.items()))] 
tokenized_data = [w for w in tokenized_data if w not in low_freq_words]

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


_word_set = list(chain.from_iterable(tokenized_data))
_fdist = nltk.FreqDist(_word_set)
#low_freq_words = [ w[0] for w in list(filter(lambda x: x[1]==1, fdist.items()))] 
#tokenized_data = [w for w in tokenized_data if w not in low_freq_words]

print("total of words: %d " % len(_word_set))
print("Word Freq distribution: ")
for w,f in _fdist.most_common(20):
	print('{};{}'.format(w,f))

#low_freq_words = [ item[0] for item in fdist.items()]

