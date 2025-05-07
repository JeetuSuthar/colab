
import nltk
nltk.download('all')
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords

text="Thala for a reason . Virat Kohli low strike rating . MSD pinging strongest stronger greatest"

tokens_sent=sent_tokenize(text)
print(tokens_sent)

tokens_words=word_tokenize(text)
print(tokens_words)

from nltk.stem import PorterStemmer
stem=[]
for i in tokens_words:
  ps=PorterStemmer()
  stem_word=ps.stem(i)
  stem.append(stem_word)
print(stem)

from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmatized_output=' '.join([lemmatizer.lemmatize(w) for w in stem])
print(lemmatized_output)

leme=[]
for i in stem:
  lemetized_word=lemmatizer.lemmatize(i)
  leme.append(lemetized_word)
print(leme)

print("POS",nltk.pos_tag(leme))

sw=stopwords.words('english')
print(sw)

words=[word for word in text.split() if word.lower() not in sw]
new_text=" ".join(words)
print(new_text)

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform([new_text])
print(tfidf_matrix.toarray())

#OPTIONAL
import pandas as pd
df = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf.get_feature_names_out())
print(df)
