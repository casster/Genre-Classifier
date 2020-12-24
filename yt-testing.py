from ids import yt_key
from googleapiclient.discovery import build


def getTracklist(description):
    if ("tracklist" or "track list" or "track-list") in description.lower():
        index = description.lower().index("0:00")
        print(description[index:])

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
#print(description)
getTracklist(description)
