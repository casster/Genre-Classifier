import requests
import base64
from ids import client_id
from ids import client_secret

def getAccessToken():
    token_url = "https://accounts.spotify.com/api/token"
    method = "POST"
    client_creds = base64.b64encode(f"{client_id}:{client_secret}".encode())
    token_data = {"grant_type" : "client_credentials"}
    token_headers = {"Authorization" : f"Basic {client_creds.decode()}"}
    r = requests.post(token_url, data=token_data, headers=token_headers)
    access_token = r.json()['access_token']
    return access_token

def doRequest(query):
    access_token = getAccessToken()
    response = requests.get(query,
        headers={"Content-Type":"application/json","Authorization":"Bearer {}".format(access_token)})
    return response

def searchForTrack(t):
    query = "https://api.spotify.com/v1/search?q="+t+"&type=track&limit=1"
    searchresponse = doRequest(query)
    if len(searchresponse.json()['tracks']['items']) == 0:
        return None
    trackid = searchresponse.json()["tracks"]["items"][0]["id"]
    return trackid

def searchForPlaylist(p):
    query = "https://api.spotify.com/v1/search?q="+p+"&type=playlist&limit=1"
    searchresponse = doRequest()
    if len(searchresponse.json()["playlists"]["items"]) == 0:
        return None
    playlistid = searchresponse.json()["playlists"]["items"][0]["id"]
    return playlistid

def getPlaylistTracks(p):
    query = "https://api.spotify.com/v1/playlists/"+p+"/tracks"
    playlistresponse = doRequest()
    tracks = []
    for t in playlistresponse.json()["items"]:
        tracks.append(t["track"]["id"])
    return tracks

def getAudioFeatures(trackid):
    query = "https://api.spotify.com/v1/audio-features/"+trackid
    trackresponse = doRequest()
    return trackresponse.json()