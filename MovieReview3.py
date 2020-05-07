Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from nltk.corpus import movie_reviews
>>> print (len(movie_reviews.fileids())) #total reviews
2000
>>> print (movie_reviews.categories()) #review categories
['neg', 'pos']
>>> print (len(movie_reviews.fileids('pos'))) #pos reviews
1000
>>> print (len(movie_reviews.fileids('neg'))) #neg reviews
1000
>>> positive_review_file = movie_reviews.fileids('pos')[0]
>>> print (positive_review_file)
pos/cv000_29590.txt
>>> documents = [] #creating a movie review document
>>> for category in movie_reviews.categories():
	for fileid in movie_reviews.fileids(category):
		documents.append((movie_reviews.words(fileid), category))

		
>>> print (len(documents))
2000
>>> x = [str(item) for item in documents[0][0]]
>>> print(x)
['plot', ':', 'two', 'teen', 'couples', 'go', 'to', 'a', 'church', 'party', ',', 'drink', 'and', 'then', 'drive', '.', 'they', 'get', 'into', 'an', 'accident', '.', 'one', 'of', 'the', 'guys', 'dies', ',', 'but', 'his', 'girlfriend', 'continues', 'to', 'see', 'him', 'in', 'her', 'life', ',', 'and', 'has', 'nightmares', '.', 'what', "'", 's', 'the', 'deal', '?', 'watch', 'the', 'movie', 'and', '"', 'sorta', '"', 'find', 'out', '.', '.', '.', 'critique', ':', 'a', 'mind', '-', 'fuck', 'movie', 'for', 'the', 'teen', 'generation', 'that', 'touches', 'on', 'a', 'very', 'cool', 'idea', ',', 'but', 'presents', 'it', 'in', 'a', 'very', 'bad', 'package', '.', 'which', 'is', 'what', 'makes', 'this', 'review', 'an', 'even', 'harder', 'one', 'to', 'write', ',', 'since', 'i', 'generally', 'applaud', 'films', 'which', 'attempt', 'to', 'break', 'the', 'mold', ',', 'mess', 'with', 'your', 'head', 'and', 'such', '(', 'lost', 'highway', '&', 'memento', ')', ',', 'but', 'there', 'are', 'good', 'and', 'bad', 'ways', 'of', 'making', 'all', 'types', 'of', 'films', ',', 'and', 'these', 'folks', 'just', 'didn', "'", 't', 'snag', 'this', 'one', 'correctly', '.', 'they', 'seem', 'to', 'have', 'taken', 'this', 'pretty', 'neat', 'concept', ',', 'but', 'executed', 'it', 'terribly', '.', 'so', 'what', 'are', 'the', 'problems', 'with', 'the', 'movie', '?', 'well', ',', 'its', 'main', 'problem', 'is', 'that', 'it', "'", 's', 'simply', 'too', 'jumbled', '.', 'it', 'starts', 'off', '"', 'normal', '"', 'but', 'then', 'downshifts', 'into', 'this', '"', 'fantasy', '"', 'world', 'in', 'which', 'you', ',', 'as', 'an', 'audience', 'member', ',', 'have', 'no', 'idea', 'what', "'", 's', 'going', 'on', '.', 'there', 'are', 'dreams', ',', 'there', 'are', 'characters', 'coming', 'back', 'from', 'the', 'dead', ',', 'there', 'are', 'others', 'who', 'look', 'like', 'the', 'dead', ',', 'there', 'are', 'strange', 'apparitions', ',', 'there', 'are', 'disappearances', ',', 'there', 'are', 'a', 'looooot', 'of', 'chase', 'scenes', ',', 'there', 'are', 'tons', 'of', 'weird', 'things', 'that', 'happen', ',', 'and', 'most', 'of', 'it', 'is', 'simply', 'not', 'explained', '.', 'now', 'i', 'personally', 'don', "'", 't', 'mind', 'trying', 'to', 'unravel', 'a', 'film', 'every', 'now', 'and', 'then', ',', 'but', 'when', 'all', 'it', 'does', 'is', 'give', 'me', 'the', 'same', 'clue', 'over', 'and', 'over', 'again', ',', 'i', 'get', 'kind', 'of', 'fed', 'up', 'after', 'a', 'while', ',', 'which', 'is', 'this', 'film', "'", 's', 'biggest', 'problem', '.', 'it', "'", 's', 'obviously', 'got', 'this', 'big', 'secret', 'to', 'hide', ',', 'but', 'it', 'seems', 'to', 'want', 'to', 'hide', 'it', 'completely', 'until', 'its', 'final', 'five', 'minutes', '.', 'and', 'do', 'they', 'make', 'things', 'entertaining', ',', 'thrilling', 'or', 'even', 'engaging', ',', 'in', 'the', 'meantime', '?', 'not', 'really', '.', 'the', 'sad', 'part', 'is', 'that', 'the', 'arrow', 'and', 'i', 'both', 'dig', 'on', 'flicks', 'like', 'this', ',', 'so', 'we', 'actually', 'figured', 'most', 'of', 'it', 'out', 'by', 'the', 'half', '-', 'way', 'point', ',', 'so', 'all', 'of', 'the', 'strangeness', 'after', 'that', 'did', 'start', 'to', 'make', 'a', 'little', 'bit', 'of', 'sense', ',', 'but', 'it', 'still', 'didn', "'", 't', 'the', 'make', 'the', 'film', 'all', 'that', 'more', 'entertaining', '.', 'i', 'guess', 'the', 'bottom', 'line', 'with', 'movies', 'like', 'this', 'is', 'that', 'you', 'should', 'always', 'make', 'sure', 'that', 'the', 'audience', 'is', '"', 'into', 'it', '"', 'even', 'before', 'they', 'are', 'given', 'the', 'secret', 'password', 'to', 'enter', 'your', 'world', 'of', 'understanding', '.', 'i', 'mean', ',', 'showing', 'melissa', 'sagemiller', 'running', 'away', 'from', 'visions', 'for', 'about', '20', 'minutes', 'throughout', 'the', 'movie', 'is', 'just', 'plain', 'lazy', '!', '!', 'okay', ',', 'we', 'get', 'it', '.', '.', '.', 'there', 'are', 'people', 'chasing', 'her', 'and', 'we', 'don', "'", 't', 'know', 'who', 'they', 'are', '.', 'do', 'we', 'really', 'need', 'to', 'see', 'it', 'over', 'and', 'over', 'again', '?', 'how', 'about', 'giving', 'us', 'different', 'scenes', 'offering', 'further', 'insight', 'into', 'all', 'of', 'the', 'strangeness', 'going', 'down', 'in', 'the', 'movie', '?', 'apparently', ',', 'the', 'studio', 'took', 'this', 'film', 'away', 'from', 'its', 'director', 'and', 'chopped', 'it', 'up', 'themselves', ',', 'and', 'it', 'shows', '.', 'there', 'might', "'", 've', 'been', 'a', 'pretty', 'decent', 'teen', 'mind', '-', 'fuck', 'movie', 'in', 'here', 'somewhere', ',', 'but', 'i', 'guess', '"', 'the', 'suits', '"', 'decided', 'that', 'turning', 'it', 'into', 'a', 'music', 'video', 'with', 'little', 'edge', ',', 'would', 'make', 'more', 'sense', '.', 'the', 'actors', 'are', 'pretty', 'good', 'for', 'the', 'most', 'part', ',', 'although', 'wes', 'bentley', 'just', 'seemed', 'to', 'be', 'playing', 'the', 'exact', 'same', 'character', 'that', 'he', 'did', 'in', 'american', 'beauty', ',', 'only', 'in', 'a', 'new', 'neighborhood', '.', 'but', 'my', 'biggest', 'kudos', 'go', 'out', 'to', 'sagemiller', ',', 'who', 'holds', 'her', 'own', 'throughout', 'the', 'entire', 'film', ',', 'and', 'actually', 'has', 'you', 'feeling', 'her', 'character', "'", 's', 'unraveling', '.', 'overall', ',', 'the', 'film', 'doesn', "'", 't', 'stick', 'because', 'it', 'doesn', "'", 't', 'entertain', ',', 'it', "'", 's', 'confusing', ',', 'it', 'rarely', 'excites', 'and', 'it', 'feels', 'pretty', 'redundant', 'for', 'most', 'of', 'its', 'runtime', ',', 'despite', 'a', 'pretty', 'cool', 'ending', 'and', 'explanation', 'to', 'all', 'of', 'the', 'craziness', 'that', 'came', 'before', 'it', '.', 'oh', ',', 'and', 'by', 'the', 'way', ',', 'this', 'is', 'not', 'a', 'horror', 'or', 'teen', 'slasher', 'flick', '.', '.', '.', 'it', "'", 's', 'just', 'packaged', 'to', 'look', 'that', 'way', 'because', 'someone', 'is', 'apparently', 'assuming', 'that', 'the', 'genre', 'is', 'still', 'hot', 'with', 'the', 'kids', '.', 'it', 'also', 'wrapped', 'production', 'two', 'years', 'ago', 'and', 'has', 'been', 'sitting', 'on', 'the', 'shelves', 'ever', 'since', '.', 'whatever', '.', '.', '.', 'skip', 'it', '!', 'where', "'", 's', 'joblo', 'coming', 'from', '?', 'a', 'nightmare', 'of', 'elm', 'street', '3', '(', '7', '/', '10', ')', '-', 'blair', 'witch', '2', '(', '7', '/', '10', ')', '-', 'the', 'crow', '(', '9', '/', '10', ')', '-', 'the', 'crow', ':', 'salvation', '(', '4', '/', '10', ')', '-', 'lost', 'highway', '(', '10', '/', '10', ')', '-', 'memento', '(', '10', '/', '10', ')', '-', 'the', 'others', '(', '9', '/', '10', ')', '-', 'stir', 'of', 'echoes', '(', '8', '/', '10', ')']
>>> print (documents[0])
(['plot', ':', 'two', 'teen', 'couples', 'go', 'to', ...], 'neg')
>>> from random import shuffle
>>> shuffle(documents) #shuffle the document list
>>> 
>>> #Feature Exctraction
>>> all_words = [word.lower() for word in movie_reviews.words()]
>>> print (all_words[:10]) #print first 10 words
['plot', ':', 'two', 'teen', 'couples', 'go', 'to', 'a', 'church', 'party']
>>> 
>>> #Creating a frequency distribution
>>> from nltk import FreqDist

>>> all_words_frequency = FreqDist(all_words)
>>> print (all_words_frequency)
<FreqDist with 39768 samples and 1583820 outcomes>
>>> print (all_words_frequency.most_common(10)) #print 10 most frequently occuring words
[(',', 77717), ('the', 76529), ('.', 65876), ('a', 38106), ('and', 35576), ('of', 34123), ('to', 31937), ("'", 30585), ('is', 25195), ('in', 21822)]
>>> 
>>> #Data Cleaning
>>> from nltk.corpus import stopwords
>>> stopwords_english = stopwords.words('english')
>>> print(stopwords_english)
['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
>>> all_words_without_stopwords = [word for word in all_words if word not in stopwords_english]
>>> print (all_words_without_stopwords[:10]) #print first 10 words
['plot', ':', 'two', 'teen', 'couples', 'go', 'church', 'party', ',', 'drink']
>>> 
>>> #Remove punctuations
>>> import string
>>> print(string.punctuation)
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
>>> all_words_without_punctuation = [word for word in all_words if word not in string.punctuation]
>>> print (all_words_without_punctuation[:10])
['plot', 'two', 'teen', 'couples', 'go', 'to', 'a', 'church', 'party', 'drink']
>>> 
>>> #Frequency Distribution of cleaned words
>>> all_words_frequency = FreqDist(all_words_clean)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    all_words_frequency = FreqDist(all_words_clean)
NameError: name 'all_words_clean' is not defined
>>> all_words_clean = []
>>> for word in all_words:
	if word not in stopwords_english and word not in string.punctuation:
		all_words_clean.append(word)



>>> 
print (all_words_clean[:10])
['plot', 'two', 'teen', 'couples', 'go', 'church', 'party', 'drink', 'drive', 'get']
>>> all_words_frequency = FreqDist(all_words_clean)
>>> 
print (all_words_frequency)
<FreqDist with 39586 samples and 710578 outcomes>
>>> print (all_words_frequency.most_common(10))
[('film', 9517), ('one', 5852), ('movie', 5771), ('like', 3690), ('even', 2565), ('good', 2411), ('time', 2411), ('story', 2169), ('would', 2109), ('much', 2049)]
>>> 
>>> #We use 2000 most frequently occurring words as the Feature
>>> print (len(all_words_frequency))
39586
>>> most_common_words = all_words_frequency.most_common(2000)
>>> print (most_common_words[:10])
[('film', 9517), ('one', 5852), ('movie', 5771), ('like', 3690), ('even', 2565), ('good', 2411), ('time', 2411), ('story', 2169), ('would', 2109), ('much', 2049)]
>>> print (most_common_words[1990:])
[('remain', 64), ('anna', 64), ('moved', 64), ('asking', 64), ('genuinely', 64), ('rain', 64), ('path', 64), ('aware', 64), ('causes', 64), ('international', 64)]
>>> word_features = [item[0] for item in most_common_words]
>>> print (word_features[:10])
['film', 'one', 'movie', 'like', 'even', 'good', 'time', 'story', 'would', 'much']
>>> 
>>> #Creating a Feature Set
>>> def document_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features

>>> #First Negative Movie review file
>>> movie_review_file = movie_reviews.fileids('neg')[0]
>>> print (movie_review_file)
neg/cv000_29416.txt
>>> print (document_features(movie_reviews.words(movie_review_file)))

>>> print (documents[0])
(['i', 'have', 'seen', 'several', '(', 'but', 'not', ...], 'pos')
>>> feature_set = []
>>> for (doc, category) in documents:
	feature_set.append((document_features(doc), category))

	

>>> 
KeyboardInterrupt
>>> print (feature_set[0])

>>> 
>>> 
>>> #Creating Train and Test Dataset
>>> print (len(feature_set))
2000
>>> test_set = feature_set[:400]
>>> train_set = feature_set[400:]
>>> print (len(train_set))
1600
>>> print (len(test_set))
400
>>> 
>>> 
>>> #Using NaiveBayesClassifier
>>> from nltk import NaiveBayesClassifier
>>> classifier = NaiveBayesClassifier.train(train_set)
>>> 
>>> #Testing the classifer
>>> from nltk import classify
>>> accuracy = classify.accuracy(classifier, test_set)
>>> print (accuracy)
0.8275
>>> 