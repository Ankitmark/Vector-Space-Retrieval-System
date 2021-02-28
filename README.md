# Vector-Space-Retrieval-System
Implementing basic vector space retrieval system and using Cranfield collection to develop and test the system.

The Cranfield collection is a standard IR text collection, consisting of 1400 documents from the
aerodynamics field, in SGML format.
Note that you also need to eliminate the SGML tags (e.g., <TITLE>, <DOC>,
<TEXT>, etc.) - only keep the actual title and text.
  
For text pre-processing, remove stopwords, perform stemming (note: if a word becomes a stopword
after stemming, please remove it), remove punctuation and numbers (replace them with “”), split
on whitespace, and remove words with one or two characters in length. Perform the same text
processing operations on both the documents and the queries.
1. Implement an indexing scheme based on the vector space model, as discussed in class. The
steps pointed out in class can be used as guidelines for the implementation. For the weighting
scheme, use and experiment with:
• TF-IDF
2. For each of the ten queries in the queries.txt file, determine a ranked list of documents,
in descending order of their cosine similarity with the query. The output of your retrieval
should be a list of (query id, document id) pairs.
Determine the average precision and recall for the ten queries, when you use:
• top 10 documents in the ranking
• top 50 documents in the ranking
• top 100 documents in the ranking
• top 500 documents in the ranking
Note: A list of relevant documents for each query is provided to you, so that you can determine
precision and recall.
