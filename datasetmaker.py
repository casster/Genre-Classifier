import json
from ids import yt_key
from googleapiclient.discovery import build
import re
from ytapi import checkTracklist, getTracklist, removeTimestamps, replaceFt
import requests
import base64
from ids import client_id
from ids import client_secret

with open('edmgenres.json') as f:
    genres = json.load(f)

dataset = open('dataset.csv','a')

token_url = "https://accounts.spotify.com/api/token"
method = "POST"
client_creds = base64.b64encode(f"{client_id}:{client_secret}".encode())

token_data = {
    "grant_type" : "client_credentials"
}
token_headers = {
    "Authorization" : f"Basic {client_creds.decode()}"
}

r = requests.post(token_url, data=token_data, headers=token_headers)
access_token = r.json()['access_token']

'''with open('dataset.csv','a') as d:
    d.write("\n1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26")'''

ytService = build('youtube', 'v3',developerKey=yt_key)

for g in genres['Genres']:
    count = 1
    searchterm = g+" mix"
    print(searchterm)
    request = ytService.search().list(
        part="snippet",
        maxResults=5,
        q=searchterm,
        type="video"
    )
    response = request.execute()

    for v in range(5):
        request2 = ytService.videos().list(
            part="snippet",
            id = response['items'][v]['id']['videoId']
        )

        response2 = request2.execute()
        description = response2['items'][v]['snippet']['description']
        if not checkTracklist(description):
            break

        print("TRACKLIST FOUND")
        trackList = getTracklist(description)
        trackList = removeTimestamps(trackList)

        for t in trackList:
            query = "https://api.spotify.com/v1/search?q="+t+"&type=track"
            searchresponse = requests.get(query,
                headers={"Content-Type":"application/json","Authorization":"Bearer {}".format(access_token)})
            print(searchresponse.json())
            trackid = searchresponse.json()["id"]
            print(searchresponse.json()['items'])

            trackresponse = requests.get("https://api.spotify.com/v1/audio-features/"+trackid,
                headers={"Content-Type":"application/json","Authorization":"Bearer {}".format(access_token)})
            rd = trackresponse.json()
            towrite = "\n"+t+","+rd["acousticness"]+","+rd["danceability"]+","+rd["energy"]+","+rd["instrumentalness"]+","+rd["loudness"]+","+rd["speechiness"]+","+rd["valence"]+","+rd["tempo"]
            for i in range(1,19):
                if i == count:
                    towrite = towrite+",1"
                else:
                    towrite = towrite+",0"
            dataset.write(towrite)
    count = count + 1