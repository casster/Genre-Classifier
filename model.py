from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import RepeatedKFold
from sklearn.metrics import accuracy_score
import numpy as np
from numpy import mean
from numpy import std
import tensorflow as tf
from tensorflow import keras
import spotifyapi as sp
import musicgenres as mg

'''data = open('dataset.csv')
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
    yset.append(yy)'''

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

def load_model():
    return tf.keras.models.load_model("saved_model/model")

def eval(search,m):
    _,_,genres = mg.load_data()
    trackid = sp.searchForTrack(search)
    if trackid == None:
        print("No track")
        return
    features = sp.getAudioFeatures(trackid)
    x = [[features['acousticness'],features["danceability"],features["energy"],features["instrumentalness"],features["loudness"],features["speechiness"],features["valence"],features["tempo"]]]
    results = m.predict(x)
    max_r = max(results[0])
    print("Most likely genre:",genres[np.where(results[0]==max_r)[0][0]],round(max_r*100,2),"%")
    for i in range(len(results[0])):
        print(genres[i],round(results[0][i]*100,2),"%")


def do():
    X, y, genres = mg.load_data()
    model = evaluate_model(X,y)
    return model





