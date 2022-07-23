from nltk.corpus import floresta, genesis, machado, gutenberg
from nltk.text import Text
from nltk.probability import FreqDist
from nltk.corpus import stopwords


# fileids() lista as obras disponíveis em cada pacote
# for i in genesis.fileids():
#     print(i)

# Lista detalhadamente cada obra
# print(genesis.readme())

_words = ''

genesis = Text(genesis.words('portuguese.txt'), name="Gênesis")

for words in genesis[:50]:
    _words += ' ' + words

print(_words.replace(';', '\n'))