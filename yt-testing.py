from ids import yt_key
from googleapiclient.discovery import build


ytService = build('youtube', 'v3',developerKey=yt_key)


request = ytService.search().list(
    part="snippet",
    maxResults=2,
    q="ateez",
    type="video"
)

response = request.execute()
print(response['items'][0]['id']['videoId'])
