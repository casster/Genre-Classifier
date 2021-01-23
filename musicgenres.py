import csv

def load_data():
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

    return Xset, yset, genres