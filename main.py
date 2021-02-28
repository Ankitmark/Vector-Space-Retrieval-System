# Ankit Kumar Singh

import preprocessing

# Creating Inv_Index for the collection
import os


def inv_index():
    invr_index = {}
    doc_no = 0
    for root, dirs, files in os.walk(os.getcwd() + "/cranfieldDocs"):
        doc_no = len(files)
        for filename in files:
            fl = open(os.getcwd() + "/cranfieldDocs/" + filename, 'r')
            text = fl.read()  # Read entire file into a string
            substring = text[text.find("<TITLE>") + len("<TITLE>"): text.find("</TITLE>")] \
                        + text[text.find("<TEXT>") + len("<TEXT>"): text.find("</TEXT>")]
            token = preprocessing.preprocessor(substring)
            fl.close()
            for a in token:
                if a in invr_index:
                    if int(filename[-4:]) in invr_index[a]:
                        invr_index[a][int(filename[-4:])] += 1
                    else:
                        invr_index[a][int(filename[-4:])] = 1
                else:
                    invr_index[a] = {int(filename[-4:]): 1}
    return invr_index, doc_no


Inv_Index, Doc_no = inv_index()


# Creating Document length
import math

def doc_len():
    dc_len = {}
    for i in Inv_Index:
        for keys in Inv_Index[i]:
            if keys in dc_len:
                dc_len[keys] = dc_len[keys] + (Inv_Index[i][keys] * math.log10(Doc_no / len(Inv_Index[i])))**2
            else:
                dc_len[keys] = (Inv_Index[i][keys] * math.log10(Doc_no / len(Inv_Index[i])))**2
    for d in dc_len:
        dc_len[d] = math.sqrt(dc_len[d])
    return dc_len


Doc_Len = doc_len()

# Creating list of lists where each inner list represent a query
with open("queries.txt") as f:
    content = f.readlines()
query = [preprocessing.preprocessor(x.strip()) for x in content]

# Creating relevant pairs of (query id, document id) from relevance.txt
with open("relevance.txt") as f:
    content = f.readlines()
list1 = [x.strip().split(" ") for x in content]
relevant = [[int(x[0]), int(x[1])] for x in list1]


# Computing precision at top k retrieved documents
def precision(relevant_l, rank_pair_l, k):
    num1 = 0
    for r in rank_pair_l[:k]:
        if r in relevant_l:
            num1 += 1
    pre = num1 / k
    return pre


# Computing recall at top k retrieved documents
def recall(relevant_l, rank_pair_l, k):
    num1 = 0
    for r in rank_pair_l[:k]:
        if r in relevant_l:
            num1 += 1
    rec = num1 / len(relevant_l)
    return rec


# Compute the cosine similarity between the document and query
def cos_sim(q):
    cos_sim1 = {}
    for term in q:
        if term in Inv_Index:
            for doc in Inv_Index[term]:
                if doc in cos_sim1:
                    cos_sim1[doc] = cos_sim1[doc] + (Inv_Index[term][doc] * math.log10(Doc_no / len(Inv_Index[term]))) \
                                   * (q.count(term) * math.log10(Doc_no / len(Inv_Index[term])))
                else:
                    cos_sim1[doc] = (Inv_Index[term][doc] * math.log10(Doc_no / len(Inv_Index[term]))) \
                                   * (q.count(term) * math.log10(Doc_no / len(Inv_Index[term])))
    for Cs in cos_sim1:
        cos_sim1[Cs] = cos_sim1[Cs] / Doc_Len[Cs]
    doc_rank = {k: v for k, v in sorted(cos_sim1.items(), key=lambda item: item[1], reverse=True)}
    rank_pair1 = [[qn, dn] for dn in doc_rank]
    return rank_pair1


pre_at_10 = []
pre_at_50 = []
pre_at_100 = []
pre_at_500 = []
rec_at_10 = []
rec_at_50 = []
rec_at_100 = []
rec_at_500 = []

# For each query get pairs of (query id, document id) from retrieved documents
# and computing precision and recall
qn = 0
for q in query:
    qn += 1
    rank_pair = cos_sim(q)
    # print(rank_pair[:10]) # To print top 10 (query id, document id) pairs
    relev_to_q = [relevant[i] for i in range(len(relevant)) if relevant[i][0] == qn]

    pre_at_10.append(precision(relev_to_q, rank_pair, 10))
    pre_at_50.append(precision(relev_to_q, rank_pair, 50))
    pre_at_100.append(precision(relev_to_q, rank_pair, 100))
    pre_at_500.append(precision(relev_to_q, rank_pair, 500))
    rec_at_10.append(recall(relev_to_q, rank_pair, 10))
    rec_at_50.append(recall(relev_to_q, rank_pair, 50))
    rec_at_100.append(recall(relev_to_q, rank_pair, 100))
    rec_at_500.append(recall(relev_to_q, rank_pair, 500))


q_no = len(query)
print("For top 10 documents in ranking\n Average precision: ",
      sum(pre_at_10)/q_no, "\n Average recall: ", sum(rec_at_10)/q_no)
print("For top 50 documents in ranking\n Average precision: ",
      sum(pre_at_50)/q_no, "\n Average recall: ", sum(rec_at_50)/q_no)
print("For top 100 documents in ranking\n Average precision: ",
      sum(pre_at_100)/q_no, "\n Average recall: ", sum(rec_at_100)/q_no)
print("For top 500 documents in ranking\n Average precision: ",
      sum(pre_at_500)/q_no, "\n Average recall: ", sum(rec_at_500)/q_no)
