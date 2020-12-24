from ids import yt_key
from googleapiclient.discovery import build


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
print(response2['items'][0]['snippet']['description'])
