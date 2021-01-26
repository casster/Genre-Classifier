from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import tensorflow as tf
import spotifyapi as sp
import musicgenres as mg


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

def load_model(m):
    return tf.keras.models.load_model(m)

def eval(search,m,g):
    trackid = sp.searchForTrack(search)
    if trackid == None:
        print("No track")
        return
    features = sp.getAudioFeatures(trackid)
    x = [[features['acousticness'],features["danceability"],features["energy"],features["instrumentalness"],features["loudness"],features["speechiness"],features["valence"],features["tempo"]]]
    results = m.predict(x)
    artists, name = sp.getTrackInfo(trackid)
    print(name, artists)
    top = np.flip(np.sort(results))[0][:5]
    for i in top:
        print(g[np.where(i==results[0])[0][0]],round(i*100,2),"%")


def do():
    X, y, genres = mg.load_data2()
    model = evaluate_model(X,y)
    return model





