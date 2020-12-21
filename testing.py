import requests
import base64
import numpy as np
from ids import client_id
from ids import client_secret

keys = ["C","C#/D♭","D","D#/E♭","E","F","F#/G♭","G","G#/A♭","A","A#/B♭","B"]
modes = ["Minor","Major"]

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

playlist_response = requests.get("https://api.spotify.com/v1/playlists/6JBqtu5GSCLMGUiQRHYZBG/tracks",
    headers={"Content-Type":"application/json","Authorization":"Bearer {}".format(access_token)})

playlist_data = playlist_response.json()
tracks = playlist_data["items"]

key_list = []
mode_list = []
keysig_list = []
dance_list = []
energy_list = []
happy_list = []

for track in tracks:
    id = track["track"]["id"]
    response = requests.get("https://api.spotify.com/v1/audio-features/"+id,
        headers={"Content-Type":"application/json","Authorization":"Bearer {}".format(access_token)})
    response_data = response.json()
    key_list.append(keys[response_data["key"]])
    mode_list.append(modes[response_data["mode"]])
    actual_key = keys[response_data["key"]]+" "+modes[response_data["mode"]]
    keysig_list.append(actual_key)
    dance_list.append(response_data["danceability"])
    energy_list.append(response_data["energy"])
    happy_list.append(response_data["valence"])

print("Average danceability = ",np.mean(dance_list)*100)
print("Average energy = ", np.mean(energy_list)*100)
print("Average happiness = ", np.mean(happy_list)*100)