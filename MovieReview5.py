from nltk.corpus import movie_reviews
print (len(movie_reviews.fileids())) #total reviews
print (movie_reviews.categories()) #review categories
print (len(movie_reviews.fileids('pos'))) #pos reviews
print (len(movie_reviews.fileids('neg'))) #neg reviews
positive_review_file = movie_reviews.fileids('pos')[0]
print (positive_review_file)
documents = [] #creating a movie review document
for category in movie_reviews.categories():
	for fileid in movie_reviews.fileids(category):
		documents.append((movie_reviews.words(fileid), category))

		
print (len(documents))
x = [str(item) for item in documents[0][0]]
print(x)
print (documents[0])
from random import shuffle
shuffle(documents) #shuffle the document list
#Feature Exctraction
all_words = [word.lower() for word in movie_reviews.words()]
print (all_words[:10]) #print first 10 words
#Creating a frequency distribution
from nltk import FreqDist
all_words_frequency = FreqDist(all_words)
print (all_words_frequency)
print (all_words_frequency.most_common(10)) #print 10 most frequently occuring words
#Data Cleaning
from nltk.corpus import stopwords
stopwords_english = stopwords.words('english')
print(stopwords_english)
all_words_without_stopwords = [word for word in all_words if word not in stopwords_english]
print (all_words_without_stopwords[:10]) #print first 10 words
#Remove punctuations
import string
print(string.punctuation)
all_words_without_punctuation = [word for word in all_words if word not in string.punctuation]
print (all_words_without_punctuation[:10])
#Frequency Distribution of cleaned words
all_words_clean = []
for word in all_words:
	if word not in stopwords_english and word not in string.punctuation:
		all_words_clean.append(word)
print (all_words_clean[:10])
all_words_frequency = FreqDist(all_words_clean)
print (all_words_frequency)
print (all_words_frequency.most_common(10))
#We use 2000 most frequently occurring words as the Feature
print (len(all_words_frequency))
most_common_words = all_words_frequency.most_common(2000)
print (most_common_words[:10])
print (most_common_words[1990:])
word_features = [item[0] for item in most_common_words]
print (word_features[:10])
#Creating a Feature Set
def document_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features
#First Negative Movie review file
movie_review_file = movie_reviews.fileids('neg')[0]
print (movie_review_file)
print (document_features(movie_reviews.words(movie_review_file)))
print (documents[0])
feature_set = []
for (doc, category) in documents:
	feature_set.append((document_features(doc), category))
print (feature_set[0])
#Creating Train and Test Dataset
print (len(feature_set))
test_set = feature_set[:400]
train_set = feature_set[400:]
print (len(train_set))
print (len(test_set))
#Using NaiveBayesClassifier
from nltk import NaiveBayesClassifier
classifier = NaiveBayesClassifier.train(train_set)
#Testing the classifer
from nltk import classify
accuracy = classify.accuracy(classifier, test_set)
print (accuracy)
#Using some custom Reviews to train the ML model
from nltk.tokenize import word_tokenize
custom_review = "I hated the film. It was a disaster. Poor direction, bad acting."
custom_review_tokens = word_tokenize(custom_review)
custom_review_set = document_features(custom_review_tokens)
print (classifier.classify(custom_review_set))
#Hence negative review correctly classified as neg
#probability result
prob_result = classifier.prob_classify(custom_review_set)
print (prob_result)
print (prob_result.max())
print (prob_result.prob("neg"))
print (prob_result.prob("pos"))
#Testing a positive review
custom_review = "It was a wonderful and amazing movie. I loved it. Best direction, good acting."
custom_review_tokens = word_tokenize(custom_review)
custom_review_set = document_features(custom_review_tokens)
print (classifier.classify(custom_review_set))
#Positive review has been classified as neg
#Feature set needs to be improved
#probability result
prob_result = classifier.prob_classify(custom_review_set)
print (prob_result)
print (prob_result.max())
print (prob_result.prob("neg"))
print (prob_result.prob("pos"))
#Show 5 most informative features
print (classifier.show_most_informative_features(10))
from nltk.corpus import movie_reviews
pos_reviews = []
for fileid in movie_reviews.fileids('pos'):
	words = movie_reviews.words(fileid)
	pos_reviews.append(words)
neg_reviews = []
for fileid in movie_reviews.fileids('neg'):
	words = movie_reviews.words(fileid)
	neg_reviews.append(words)
print (pos_reviews[0])
print (neg_reviews[0])
print (pos_reviews[0][:20])
print (neg_reviews[0][:20])
#Feature Extracton
from nltk.corpus import stopwords
import string
stopwords_english = stopwords.words('english')
def bag_of_words(words): #feature extraction function
	words_clean = []
	for word in words:
		word = word.lower()
		if word not in stopwords_english and word not in string.punctuation:
			words_clean.append(word)
	words_dictionary = dict([word, True] for word in words_clean)
	return words_dictionary
print (bag_of_words(['the', 'the', 'good', 'bad', 'the', 'good']))
#Creating a feature set
pos_reviews_set = []
for words in pos_reviews:
	pos_reviews_set.append((bag_of_words(words), 'pos'))
neg_reviews_set = []
for words in neg_reviews:
	neg_reviews_set.append((bag_of_words(words), 'neg'))
print (pos_reviews_set[0])
print (neg_reviews_set[0])
#Creating Train and Test set
print (len(pos_reviews_set), len(neg_reviews_set)) # Output: (1000, 1000)
from random import shuffle
#Different output accuracy everytime we run the program
shuffle(pos_reviews_set)
shuffle(neg_reviews_set)
test_set = pos_reviews_set[:200] + neg_reviews_set[:200]
train_set = pos_reviews_set[200:] + neg_reviews_set[200:]
print(len(test_set),  len(train_set))
#Training the Classifier
from nltk import classify
from nltk import NaiveBayesClassifier
classifier = NaiveBayesClassifier.train(train_set)
accuracy = classify.accuracy(classifier, test_set)
print(accuracy)
print (classifier.show_most_informative_features(10))
#Testing Classifier with Custom Review
from nltk.tokenize import word_tokenize
custom_review = "I hated the film. It was a disaster. Poor direction, bad acting."
custom_review_tokens = word_tokenize(custom_review)
custom_review_set = bag_of_words(custom_review_tokens)
print (classifier.classify(custom_review_set))
prob_result = classifier.prob_classify(custom_review_set)
print (prob_result)
print (prob_result.max())
print (prob_result.prob("neg"))
print (prob_result.prob("pos"))
custom_review = "It was a wonderful and amazing movie. I loved it. Best direction, good acting."
custom_review_tokens = word_tokenize(custom_review)
custom_review_set = bag_of_words(custom_review_tokens)
print (classifier.classify(custom_review_set))
prob_result = classifier.prob_classify(custom_review_set)
print (prob_result)
print (prob_result.max())
print (prob_result.prob("neg"))
print (prob_result.prob("pos"))
classifier = nltk.NaiveBayesClassifier.train(train_set)
print('Accuracy: {:4.2f}'.format(nltk.classify.accuracy(classifier, test_set)))
from sklearn import cross_validation
model = RandomForestClassifier(n_estimators=100) #Simple K-Fold cross validation
cv = cross_validation.KFold(len(train), n_folds=5, indices=False)
results = []
probas = model.fit(train[traincv], target[traincv])
predict_proba(train[testcv])
results.append( Error_function )
print ("Results: " + str( np.array(results).mean() ))