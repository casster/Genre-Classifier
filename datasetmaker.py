import json

import re
import ytapi as yt
import spotifyapi as sp
import csv


with open('edmgenres.json') as f:
    genres = json.load(f)

dataset = open('dataset.csv','a')


'''with open('dataset.csv','a') as d:
    d.write("\n1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26")'''

'''count = 16
for g in genres['Genres']:
    if g == "Bass music" or g == "Breakbeat" or g == "Disco" or g == "Downtempo" or g =="Drum and bass" or g == "Electronic rock" or g == "Jungle" or g =="Hardcore" or g=="Hardstyle" or g == "Hauntology" or g == "Hip hop fusion" or g == "Trap" or g == "House" or g == "Industrial" or g == "Techno":
        continue
    searchterm = g+" mix"
    print(searchterm)
    #print(yt.getTracksForDataset(searchterm))
    tracks = yt.getTracksForDataset(searchterm)
    for t in tracks:
        with open('songs.csv','a') as s:
            s.write("\n"+t)
            for i in range(1,18):
                if count == i:
                    s.write(",1")
                else:
                    s.write(",0")
    count = count+1'''

songs = open('songs2.csv')
reader = csv.DictReader(songs)

for row in reader:
    song = row['song']
    print(song)
    trackid = sp.searchForTrack(song)
    if trackid == None:
        continue
    features = sp.getAudioFeatures(trackid)
    dataset.write("\n"+song)
    dataset.write(","+str(features['acousticness'])+","+str(features["danceability"])+","+str(features["energy"])+","+str(features["instrumentalness"])+","+str(features["loudness"])+","+str(features["speechiness"])+","+str(features["valence"])+","+str(features["tempo"]))
    dataset.write(","+row["bassmusic"]+","+row["breakbeat"]+","+row["disco"]+","+row["downtempo"]+","+row["dnb"]+","+row["erock"]+","+row["jungle"]+","+row["hardcore"]+","+row["hardstyle"]+","+row["hauntology"]+","+row["hip hop fusion"]+","+row["trap"]+","+row["house"]+","+row["industrial"]+","+row["techno"]+","+row["trance"]+","+row["uk garage"])
