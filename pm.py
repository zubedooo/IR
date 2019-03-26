import operator

N=10
documents=[]
for i in range(10):
    searchfile = open("freq-t"+str(i+1)+".txt", "r")
    doci=[]
    for line in searchfile:
        line=line.split(":")
        doci.append(line[0])
    documents.append(doci)
    searchfile.close()
print(documents)

Nw=dict()
docs=[]
for i in range(10):
    docs=docs+documents[i]

docs=list(set(docs))

def compute(Nw):
    return (N-Nw+0.5)/(Nw+0.5)

table=dict()
for x in docs:
    nw=0
    list1=[]
    for i in documents:
        if x in i:
            nw+=1
    list1.append(nw)
    calc=compute(nw)
    list1.append(calc)
    table[x]=list1
print(table)

query=input("Enter query :").split(" ")

pd=dict()

for i in range(N):
    pdi=1
    for x in query:
        if x in documents[i]:
            pdi=pdi*table[x][1]
    pd[i+1]=pdi

sorted_x = sorted(pd.items(), key=operator.itemgetter(1),reverse=True)

print(sorted_x)