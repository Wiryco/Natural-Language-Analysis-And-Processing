from unicodedata import category
import nltk
from nltk.corpus import brown
from nltk.corpus import gutenberg

#print(brown.categories())

words_religion = brown.words(categories='religion')
words_mystery = brown.words(categories='mystery')

fdist = nltk.FreqDist(w.lower() for w in words_religion)

for i in words_religion[0:100]:
    print(i)