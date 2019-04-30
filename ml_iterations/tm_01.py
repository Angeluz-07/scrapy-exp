import re #Regex
import nltk
import json
from gensim import models, corpora

from itertools import chain

###
# II iteration of my learning of topic modelling
# desc.: tokenization, stopword removal, LDA, word frecuency.

#number of topics to look for
NUM_TOPICS = 10

#getting stop_words from nltk
stop_words = nltk.corpus.stopwords.words('english')
exclude = ['elixir','software','use','web','development']
stop_words.extend(exclude)

#input must be a string (a line, a paragraph,...)
def clean_text(text):
	#tokenize, returns a list	
	tokenized_text = nltk.word_tokenize(text.lower())
	#remove stopwords
	cleaned_text = [t for t in tokenized_text if t.lower() not in stop_words and re.match('[a-zA-Z\-][a-zA-Z\-]{2,}',t)]

	return cleaned_text

#getting my data from json file
#this data contains description about a set of companies using certain technology
file_path = '../scraped_data/elixir_companies.json'
with open(file_path) as f:
	data = json.load(f)

#checking out data
#print(json.dumps(data, indent = 4))
#print(data)

#For genism we nee to tokenize data and filter out stopwords
tokenized_data = []
for company in data:
	text = company['description']
	tokenized_data.append(clean_text(text))

#print(tokenized_data[:3])

#Build a dictionary - associate word to numeric id
dictionary = corpora.Dictionary(tokenized_data)
print(len(list(dictionary.values())))

#Transform collection of text to numerical form
corpus = [dictionary.doc2bow(text) for text in tokenized_data]
#print first document looks like
#print(corpus[0])

#Build the LDA model
lda_model = models.LdaModel(corpus = corpus, num_topics = NUM_TOPICS, id2word = dictionary)

print("LDA model: ")
for idx in range(NUM_TOPICS):
	#print("Topic #%s" % idx, lda_model.print_topic(idx,10))	
	#print("Topic #%s" % idx, lda_model.show_topic(idx,10))
	topic_summary = ' '.join([ v[0] for v in lda_model.show_topic(idx,10) ])
	print("Topic #%s : %s " % (idx, topic_summary))
		
print("=" * 20)

#see frequency distribution of words
#to remove either stopwords in the context of the documents
#or very low frequency words

#this receives a list of all the words in the documents
word_set = list(chain.from_iterable(tokenized_data))
fdist = nltk.FreqDist(word_set)

print("word freq dist: ")
for w,f in fdist.most_common(10):
	print('{};{}'.format(w,f))

#fdist.plot(50)
