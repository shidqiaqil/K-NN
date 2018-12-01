import csv
import math
train = []
test = []
hsl = []
k=6
#memasukkan file csv

with open('DataTrain_Tugas3_AI.csv','r') as f:
    datafile = csv.reader(f,delimiter=',')
    for data in datafile:
        train.append(data)
train.pop(0)
with open('DataTest_Tugas3_AI.csv','r') as t:
    datafile = csv.reader(t,delimiter=',')
    for data in datafile:
        test.append(data)
test.pop(0)

def take(e):
    return e[0]
def hitung (a,b):
    return float(a) - float(b)
def jumlah(a,b):
    return math.pow( hitung(a, b) ,2)
def eucdist (x, y):
    jum=0
    for i in range(1,6):
        jum+=jumlah(x[i],y[i])
    return math.sqrt(jum)

def getterbanyak(b):
    a=[]
    for i in range(0,4):
        a.append([0 if b.get(str(i))==None else b.get(str(i)),i])
    a.sort(key=take,reverse=True)
    return a[0][1]

def voting():
    jarakterdekat=[]
    for l in range(0,k):
        jarakterdekat.append(hsl[l][1])
    b= {i:jarakterdekat.count(i) for i in jarakterdekat}
    return getterbanyak(b)

def sort():
    hsl.sort(key=take)

for i in range(0,len(test)):
    for j in range(0,len(train)):
        hsl.append( [eucdist(train[j], test[i]),train[j][6]] )
    sort()
    test[i][6]=voting()
    hsl.clear()
#for i in range(0,len(test)):
#    print(test[i][6])
with open('TebakanTugas3.csv','w',newline='\n') as f:
    datafile = csv.writer(f,dialect='excel')
    for i in range(0,len(test)):
        datafile.writerow([test[i][6]])
f.close()
