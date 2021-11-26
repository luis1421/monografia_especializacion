import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

class Document:
    """A class for text analysis
        :param data: list of dicts
        :param variable_name: variable name to be analyzed
        :ivar text: string of text to be analyzed; set by `text` parameter
        """
    # Class attribute    
    english_stops = stopwords.words('english')

    def __init__(self, data, variable_name):
        self.data = data
        self.variable_name = variable_name
        self.tokens = self._tokenize()
        self.word_counts = self._count_words()
        

    def _tokenize(self):
        tokens = []
        for i in self.data:
            wt = word_tokenize(i[self.variable_name])
            lower_tokens = [t.lower() for t in wt]
            alpha_only = [t for t in lower_tokens if t.isalpha()]
            #english_stops = stopwords.words('english')
            no_stops = [t for t in alpha_only if t not in Document.english_stops]
            tokens += no_stops
        return tokens
    
    def _count_words(self):
        return Counter(self.tokens)
    
