import csv

def strToNum(X,y):
    Xset = []
    yset = []
    for i in X:
        xx = []
        for j in i:
            xx.append(float(j))
        Xset.append(xx)

    for i in y:
        yy = []
        for j in i:
            yy.append(int(j))
        yset.append(yy)
    return Xset, yset


def load_data1():
    data = open('dataset.csv')
    reader = csv.reader(data)
    X = []
    y = []
    for row in reader:
        X.append(row[1:9])
        y.append(row[9:])

    genres = y[0]

    X = X[1:]
    y = y[1:]

    Xset, yset = strToNum(X,y)

    return Xset, yset, genres

def load_data2():
    dataset = open("dataset3.csv")
    reader = csv.reader(dataset)
    X = []
    y = []
    for row in reader:
        X.append(row[0:8])
        y.append(row[8:])

    genres = y[0]
    X = X[1:]
    y = y[1:]
    
    Xset, yset = strToNum(X,y)

    return Xset, yset, genres