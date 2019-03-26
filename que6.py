rQ = [3, 5, 9, 25, 39, 44, 56, 71, 89, 94, 105, 119, 124, 136, 144]
aQ = [123, 84, 56, 6, 8, 777, 511, 129, 187, 25, 38, 48, 250, 113, 44, 99, 95, 214, 136, 39, 128, 71, 14, 5]
p = {}
r = {}
relevant = 0
for i in range(len(aQ)):
    doc = aQ[i]
    if (doc in rQ):
        relevant += 1;
        p[doc] = relevant / (i + 1) * 100
        r[doc] = relevant / len(rQ) * 100

print("Precision of relevant docs : \n", p)
print("Recall of relevant docs \n: ", r)

keysR = r.keys()
keys30 = []
keys60 = []
keys90 = []
values = []
for i in keysR:
    if (r[i] <= 30.0):
        keys30.append(i)
    if (r[i] > 30.0 and r[i] <= 60.0):
        keys60.append(i)
    if (r[i] > 60.0 and r[i] <= 90.0):
        keys90.append(i)

for i in keys30:
    values.append(p[i])
if not values:
    print("Interpolated precision at 30% is : 0")
else:
    print("Interpolated precision at 30% is : ", max(values))

values.clear()
for i in keys60:
    values.append(p[i])
if not values:
    print("Interpolated precision at 60% is : 0")
else:
    print("Interpolated precision at 60% is : ", max(values))
values.clear()
for i in keys90:
    values.append(p[i])
if not values:
    print("Interpolated precision at 90% is : 0")
else:
    print("Interpolated precision at 90% is : ", max(values))
count=0
for i in range(len(rQ)):
    if aQ[i] in rQ:
       count+=1
print("R Precision : " + str(count*100/(len(rQ))))

def harmonic_mean(a,b):
    return 2/((100/a)+(100/b))
hm={}
for doc in p:
    hm[doc]=harmonic_mean(p[doc],r[doc])

print("Harmonic Mean :")
print(hm)
b=[0.5,1,2]
def Emeasure(r,p,b):
    Em=[]
    for i in b:
        if i<1:
            Em.append(1-((1+i*i)/((i*i*100)/r)+(100/p)))
        if i==1:
            Em.append(1-harmonic_mean(r,p))
        if i>1:
            Em.append(1 - ((1 + i * i) / ((i * i) / r) + (1 / p)))
    return Em
Em={}
for doc in p:
    Em[doc]=Emeasure(r[doc],p[doc],b)
print("E measure : ")
print(Em)