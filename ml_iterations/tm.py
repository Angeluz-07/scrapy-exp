import nltk
import json
from gensim import models, corpora

###
# I iteration of my learning of topic modelling
# desc.: tokenization, stopword removal, lda.

file_path = '../scraped_data/elixir_companies.json'
with open(file_path) as f:
	data = json.load(f)

#checking out data
#print(json.dumps(data, indent = 4))
#print(data)

#taking first paragraph to experiment
first_text = data[0]['description']
#print(first_text)

###TOKENIZATION
first_text_list = nltk.word_tokenize(first_text)
print(first_text_list)
print()

###STOPWORDS REMOVAL
#getting stop_words from nltk
stop_words = nltk.corpus.stopwords.words('english')

#removing stopwords from my list
first_text_list_cleaned = [w for w in first_text_list if w.lower() not in stop_words]
print(first_text_list_cleaned)
print()


tokenized_data = [first_text_list_cleaned]
#Build a dictionary - associate word to numeric id
dictionary = corpora.Dictionary(tokenized_data)

#Transform collection of text to numerical form
corpus = [dictionary.doc2bow(text) for text in tokenized_data]
print(corpus[0])


NUM_TOPICS = 10
#build the lda model
lda_model = models.LdaModel(corpus = corpus, num_topics = NUM_TOPICS, id2word = dictionary)

print("LDA model: ")

for idx in range(NUM_TOPICS):
	print("Topic #%s" % idx, lda_model.print_topic(idx,10))

print("=" * 20)
