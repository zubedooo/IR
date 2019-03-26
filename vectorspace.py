import math
import operator
n=10
documents=[]
keywords=[]
for i in range(10):
    searchfile = open("freq-t"+str(i+1)+".txt", "r")
    doci=[]
    for line in searchfile:
        line=line.split(":")
        doci.append(line[0])
    documents.append(doci)
    searchfile.close()
print(documents)
def freqs(str1):
    #str_list = str1.split()
    dict1=dict()
    unique_words = set(str1)

    for words in unique_words:
        words = words.lower()
        dict1[words]=str1.count(words)
    return dict1

for i in documents:
    keywords=keywords+i
print(keywords)
freq=freqs(keywords)
print(freq)


idf=dict()
#for x in freq:
 #   idf[x]=math.log(n/freq[x],2)
tf_idf=dict()
for x in freq:
    if freq[x]==0:
        continue
    tf_idf_x=[]
    idf[x] = math.log(n / freq[x], 2)
    for i in range(n):
        if x in documents[i]:
            tf_idf_x.append(1*idf[x])
        else:
            tf_idf_x.append(0)
    tf_idf[x]=tf_idf_x
print("tf-idf :")
print(tf_idf)

query=input("Enter query :").split(" ")
freq_q=freqs(query)

tf_idf_q=dict()
for y in freq:
    if y in query:
        tf_idf_q[y]=((freq_q[y]/max(freq_q.values()))*idf[y])
    else:
        tf_idf_q[y]=0
print(tf_idf_q)

def Length(param):
    sum=0
    for i in param:
        sum=sum+(i*i)
    return math.sqrt(sum)

doclength=[]
docidf=[]

for i in range(n):
    temp=[]
    for x in tf_idf:
        temp.append(tf_idf[x][i])
    docidf.append(temp)
    doclength.append(Length(docidf[i]))
q_length=Length(list(tf_idf_q.values()))
print("Document and query lengths :")
print(doclength)
print(q_length)

sim={}
for i in range(n):
    sum=0
    for x in tf_idf:
        sum=sum+(tf_idf[x][i]*tf_idf_q[x])
    sum=sum/(doclength[i]*q_length)
    sim[i+1]=sum
print("Ranking of documents : ")
print(sorted(sim.items(),key=operator.itemgetter(1),reverse=True))

sim_matrix=[]

for i in range(n):
    sim_i = []
    for j in range(n):
        sum=0
        if i==j:
            sum=1
            sim_i.append(sum)
            continue
        for x in tf_idf:
            sum = sum + (tf_idf[x][i] * tf_idf[x][j])
        sum = sum / (doclength[i] * doclength[j])
        sim_i.append(sum)
    sim_matrix.append(sim_i)
print ("Similarity matrix : ")
for i in sim_matrix:
    print(i)