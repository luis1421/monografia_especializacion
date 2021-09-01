from text_analyzer.utils import counter_len
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams
from collections import Counter

class Document:
    """A class for text analysis

        :param data: list of dicts
        :param variable_name: variable name to be analyzed
        :param n: number of n-grams
        :ivar text: string of text to be analyzed; set by `text` parameter
        """
    # Class attribute    
    english_stops = stopwords.words('english')

    def __init__(self, data, variable_name, n):
        self.data = data
        self.variable_name = variable_name
        self.n = n
        self.tokens = self._tokenize()[0]
        self.n_grams = self._tokenize()[1]
        self.word_counts = self._count_words()
        self.word_len = self._len_word()
        
    def _tokenize(self):
        tokens = []
        n_grams = []
        for i in self.data:
            try:
                wt = word_tokenize(i[self.variable_name])
                lower_tokens = [t.lower() for t in wt]
                alpha_only = [t for t in lower_tokens if t.isalpha()]
                ng = ngrams(alpha_only, self.n) 
                n_grams += ng
                no_stops = [t for t in alpha_only if t not in Document.english_stops]
                tokens += no_stops       
            except KeyError:
                continue
        return tokens, n_grams
    
    def _count_words(self):
        return Counter(self.tokens)
    
    def _len_word(self):
        return counter_len(self.tokens)
    
