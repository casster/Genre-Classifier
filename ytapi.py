from ids import yt_key
from googleapiclient.discovery import build
import re

def checkTracklist(description):
    if ("tracklist" or "track list" or "track-list") in description.lower():
        return True
    return False


def getTracklist(description):
    if checkTracklist(description):
        if "0:00" in description:
            index = description.lower().index("0:00")
            return description[index:]
        else:
            description = description[description.lower().index("track"):]
            if "1." in description:
                index = description.lower().index("1.")
                return description[index:]
            elif "1:" in description:
                index = description.lower().index("1:")
                return description[index:]

def removeTimestamps(tracklist):
    tracks = tracklist.split('\n')
    newTracklist = []
    if "0:00" in tracklist:
        for track in tracks:
            if len(track) == 0:
                break
            #print("TRACK ",track)
            index = re.search("(([0-9]:|[0-9]{2}:)+[0-9]{2})",track).span()[1]
            newTrack = track[index+1:]
            #Because spotify has features as .feat
            newTrack = replaceFt(newTrack)
            newTracklist.append(newTrack)
        return newTracklist
    elif ("1." or "1:") in tracklist:
        for track in tracks:
            if len(track) == 0:
                break
            index = re.search("([0-9]+(.|:))",track).span()[1]
            newTrack = track[index+1:]
            newTrack = replaceFt(newTrack)
            newTracklist.append(newTrack)
        return newTracklist


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
    search = genre + " mix"
    ids = getVideoIDs(search,5)
    print(ids)
    tracks = []
    for i in ids:
        description = getVideoDescription(i)
        if checkTracklist(description):
            tracklist = getTracklist(description)
            tracklist = removeTimestamps(tracklist)
            tracks = tracks + tracklist
    print(tracks)
    