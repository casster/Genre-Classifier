import json

import re
import ytapi as yt
import spotifyapi as sp
import csv
import genres as g
dataset = open('dataset3.csv','a')
count =119
for genre in g.genres[119:]:
    print(genre)
    playlist = sp.searchForPlaylist(genre)
    if playlist ==  None:
        continue
    tracks = sp.getPlaylistTracks(playlist)
    for t in tracks:
        if t == None:
            continue
        features = sp.getAudioFeatures(t)
        if "error" in features:
            continue
        with open('dataset3.csv','a') as s:
            s.write("\n"+str(features['acousticness'])+","+str(features["danceability"])+","+str(features["energy"])+","+str(features["instrumentalness"])+","+str(features["loudness"])+","+str(features["speechiness"])+","+str(features["valence"])+","+str(features["tempo"]))
            for i in range(120):
                if count == i:
                    s.write(",1")
                else:
                    s.write(",0")
    count = count+1


'''with open('dataset.csv','a') as d:
    d.write("\n1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26")'''

'''count = 1
for g in genres['Genres']:
    print(g)
    playlist = sp.searchForPlaylist(g)
    if playlist ==  None:
        continue
    tracks = sp.getPlaylistTracks(playlist)
    for t in tracks:
        with open('songs2.csv','a') as s:
            s.write("\n"+t)
            for i in range(1,18):
                if count == i:
                    s.write(",1")
                else:
                    s.write(",0")
    count = count+1

songs = open('songs2.csv')
reader = csv.DictReader(songs)

for row in reader:
    songid = row['songid']
    print(songid)
    features = sp.getAudioFeatures(songid)
    dataset.write("\n"+songid)
    dataset.write(","+str(features['acousticness'])+","+str(features["danceability"])+","+str(features["energy"])+","+str(features["instrumentalness"])+","+str(features["loudness"])+","+str(features["speechiness"])+","+str(features["valence"])+","+str(features["tempo"]))
    dataset.write(","+row["bassmusic"]+","+row["breakbeat"]+","+row["disco"]+","+row["downtempo"]+","+row["dnb"]+","+row["erock"]+","+row["jungle"]+","+row["hardcore"]+","+row["hardstyle"]+","+row["hauntology"]+","+row["hip hop fusion"]+","+row["trap"]+","+row["house"]+","+row["industrial"]+","+row["techno"]+","+row["trance"]+","+row["uk garage"])'''
