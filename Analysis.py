from textblob import TextBlob
import nltk
from newspaper import Article
url = 'https://www.amazon.in/gp/customer-reviews/R1TY1VXRR562P8/ref=cm_cr_dp_d_rvw_ttl?ie=UTF8&ASIN=B07PFFMP9P'
article = Article(url)
article.download()
article.parse()
nltk.download('punkt')
article.nlp()
text = article.summary
print(text)
obj = TextBlob(text)
#returns the sentiment of text
#by returning a value between -1.0 and 1.0
sentiment = obj.sentiment.polarity
print(sentiment)
if sentiment == 0:
  print('The text is neutral')
elif sentiment > 0:
  print('The text is positive')
else:
  print('The text is negative')
