from ids import yt_key
from googleapiclient.discovery import build
import re


def getTracklist(description):
    if ("tracklist" or "track list" or "track-list") in description.lower():
        index = description.lower().index("0:00")
        return description[index:]

def removeTimestamps(tracklist):
    tracks = trackList.split('\n')
    newTracklist = []
    for track in tracks:
        index = re.search("(([0-9]:|[0-9]{2}:)+[0-9]{2})",track).span()[1]
        newTrack = track[index+1:]
        newTrack = replaceFt(newTrack)
        newTracklist.append(newTrack)
    return newTracklist

def replaceFt(track):
    return re.sub("ft","feat",track)


ytService = build('youtube', 'v3',developerKey=yt_key)


request = ytService.search().list(
    part="snippet",
    maxResults=2,
    q="melodic dubstep mix",
    type="video"
)

response = request.execute()
print(response['items'][0]['id']['videoId'])
request2 = ytService.videos().list(
    part="snippet",
    id = response['items'][0]['id']['videoId']
)

response2 = request2.execute()
description = response2['items'][0]['snippet']['description']

trackList = getTracklist(description)
trackList = removeTimestamps(trackList)
print(trackList)