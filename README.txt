Name: Ankit Kumar Singh


Instruction to run the project:
This project is build with the Pycharm IDE. Hence to run the main.py the First_Project folder can be opened and run with Pycharm.


Functions and functionality:

preprocessor(file_str):
Takes string as input and it remove punctuatoin, tokenize on whitespace, perform stemming, remove string of length less than 3,
remove stopword before stemming and after stemming and return the token list .

def precision(relevant_l, rank_pair_l, k):
Takes list of relevent documents as list of pair (query id, document id) and the retrieved ranked list of document for each query and a intiger k.
Computes the precision for the top k documents.

def recall(relevant_l, rank_pair_l, k):
Takes list of relevent documents as list of pair (query id, document id) and the retrieved ranked list of document for each query and a intiger k.
Computes the recall for the top k documents.

def inv_index():
This function create and return inverted index as hashtable from the whole collection, where keys are tokens and values are the hashtable of documents
and its token frequency. This function also return total number of documents in the collection.

def doc_len():
This function create and return document length as hashtable where documents IDs are the keys and the document length are the values.

def cos_sim(q):
This function takes query as list of query tokens and create a hashtable with cosine similarity between documents and query.
once the hashtable is created it sortes it in reverse order and create a ranked list of (query id, document id) in descending order.


Answers to the Questions:

For top 10 documents in ranking
 Average precision:  0.21000000000000002 
 Average recall:  0.19720760233918128
For top 50 documents in ranking
 Average precision:  0.10200000000000001 
 Average recall:  0.43461988304093574
For top 100 documents in ranking
 Average precision:  0.06799999999999999 
 Average recall:  0.5384210526315789
For top 500 documents in ranking
 Average precision:  0.023600000000000003 
 Average recall:  0.9430555555555555


