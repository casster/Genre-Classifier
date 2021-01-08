from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import RepeatedKFold
from sklearn.metrics import accuracy_score
import csv
from numpy import mean
from numpy import std

data = open('dataset.csv')
reader = csv.reader(data)
X = []
y = []
for row in reader:
    X.append(row[1:9])
    y.append(row[9:])

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

def get_model(n_inputs, n_outputs):
    model = Sequential()
    model.add(Dense(20, input_dim=n_inputs, kernel_initializer='he_uniform', activation='relu'))
    model.add(Dense(n_outputs, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam')
    return model
    


def evaluate_model(X, y):
    n_inputs, n_outputs = len(X[1]), len(y[1])
    model = get_model(n_inputs, n_outputs)
    model.fit(X, y, verbose=0, epochs=100)
    return model

def do():
    print(X[0])
    print(y[0])
    model = evaluate_model(Xset,yset)
    return model





