# Ankit Kumar Singh

from string import punctuation
from nltk.tokenize import WhitespaceTokenizer
from nltk.stem import PorterStemmer

tk = WhitespaceTokenizer()
ps = PorterStemmer()

# Creating stop word list
with open("stopwords.txt") as f:
    content = f.readlines()
stop_words = [x.strip() for x in content]


# Preprocessing string
def preprocessor(file_str):
    lo_file_str = file_str.lower()  # lower casing
    words = ''.join(
        c for c in lo_file_str if c not in punctuation and not c.isdigit())  # remove punctuation and numbers
    tok = tk.tokenize(words)  # tokenize on whitespace
    l_tokens = [t for t in tok if len(t) > 2]  # remove words with one or two characters
    b_filtered_tok = [w for w in l_tokens if not w in stop_words]  # Removing Stopwords (before stemming)
    stemmed_l = []
    for w in b_filtered_tok:
        stemmed_l.append(ps.stem(w))  # Stemming
    filtered_tok = [w for w in stemmed_l if not w in stop_words]  # Removing Stopwords (after stemming)
    return filtered_tok
