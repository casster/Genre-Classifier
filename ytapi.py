from ids import yt_key
from googleapiclient.discovery import build
import re

def checkTracklist(description):
    if ("tracklist" or "track list" or "track-list") in description.lower():
        return True
    return False


def getTracklist(description):
    if checkTracklist(description):
        startOfTracklist = re.search("track",description.lower()).span()[1]
        index = re.search("(\n)+",description[startOfTracklist:]).span()[1]
        tracklist = replaceFt(description[startOfTracklist:][index:])
        return tracklist

def checkForTimestamps(description):
    if "0:00" in description or "0:01" in description or "1." in description or "1:" in description:
        return True
    return False

def removeTimestamps(tracklist):
    tracks = tracklist.split('\n')
    newTracklist = []
    if checkForTimestamps(tracklist):
        if "0:00" in tracklist or "0:01" in tracklist:
            for track in tracks:
                if len(track) == 0:
                    return newTracklist
                index = re.search("(([0-9]:|[0-9]{2}:)+[0-9]{2})",track)
                if index is None:
                    return newTracklist
                index = index.span()[1]
                newTrack = track[index+1:]
                newTrack = replaceFt(newTrack)
                newTracklist.append(newTrack)
            return newTracklist
        elif ("1." or "1:") in tracklist:
            for track in tracks:
                if len(track) == 0:
                    return newTracklist
                index = re.search("([0-9]+(.|:))",track).span()[1]
                newTrack = track[index+1:]
                newTrack = replaceFt(newTrack)
                newTracklist.append(newTrack)
            return newTracklist
    else:
        return tracks


def replaceFt(track):
    return re.sub("ft","feat",track)

def getVideoIDs(query,n):
    ytService = build('youtube', 'v3',developerKey=yt_key)
    ids = []
    request = ytService.search().list(
        part="snippet",
        maxResults=n,
        q=query,
        type="video"
    )
    response = request.execute()
    for v in response['items']:
        ids.append(v['id']['videoId'])
    return ids

def getVideoDescription(id):
    ytService = build('youtube', 'v3',developerKey=yt_key)
    request = ytService.videos().list(
        part="snippet",
        id = id
    )
    response = request.execute()
    description = response['items'][0]['snippet']['description']
    return description

def getTracksForDataset(genre):
    ids = getVideoIDs(genre,5)
    tracks = []
    for i in ids:
        description = getVideoDescription(i)
        if checkTracklist(description):
            tracklist = getTracklist(description)
            tracklist = removeTimestamps(tracklist)
            if tracklist is not None:
                tracks = tracks + tracklist
    return tracks
    