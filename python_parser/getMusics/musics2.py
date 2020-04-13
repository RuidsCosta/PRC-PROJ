import os
import sys
import json
import spotipy
import webbrowser
import csv
import spotipy.util as util
from json.decoder import JSONDecodeError



username = '11156533090'

#erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

spotifyObject = spotipy.Spotify(auth=token)


user = spotifyObject.current_user()



file1 = open('artists2.txt', 'r') 
Lines = file1.readlines() 




musicForm = ""
musicCount = 1000
for name in Lines:
    searchResults = spotifyObject.search(name,1,0,"artist")
    if searchResults['artists']['items']:
        artist = searchResults['artists']['items'][0]
        artistID = artist['id']

        # Extract album data
        albumResults = spotifyObject.artist_albums(artistID)
        albumResults = albumResults['items']

        for item in albumResults:
            if item['id']:
                albumID = item['id']
                trackResults = spotifyObject.album_tracks(albumID)
                trackResults = trackResults['items']
                for music in trackResults:
                    if music['id']:
                        musicID = music['id']
                        musicForm += (f'###  http://www.semanticweb.org/ricardo/ontologies/2020/3/spotify#{musicID}\n')
                        musicForm += (f':{musicID} rdf:type owl:NamedIndividual ,\n')
                        musicForm += (f'\t\t:música ;\n')
                        
                    if len(item['id']) > 0:
                        musicForm += (f'\t:estáInseridaEm :{albumID} ;\n')
                    if len(artistID) > 0 :
                        musicForm += (f'\t:éTocadaPor :{artistID} ;\n')
                    if music['duration_ms']:
                        milli = music['duration_ms']
                        seconds=(milli/1000)
                        musicForm += (f'\t:duração {seconds} ;\n')
                    if music['explicit']:
                        exp = music['explicit']
                        musicForm += (f'\t:explícita "{exp}"^^xsd:boolean ;\n')
                    
                    if music['name']:
                        nameM = music['name']
                        musicForm += (f'\t:título "{nameM}"^^xsd:string .\n')
                    musicForm += (f'\n\n\n')
                    
    musicCount += 1
    print('Artista nr: ' + str(musicCount))





file = open("musics_formatted2.ttl", "w") 

file.write(musicForm) 

file.close()


