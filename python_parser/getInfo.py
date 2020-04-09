import os
import sys
import json
import spotipy
import webbrowser
import csv
import spotipy.util as util
from json.decoder import JSONDecodeError



#configuraçoes no terminal
# export SPOTIPY_CLIENT_ID='724cea4f9136476c8b7bc9b2539611f5'
# export SPOTIPY_CLIENT_SECRET='446203d8c1ca42ab8a58ca1fabcf2e4d'
# export SPOTIPY_REDIRECT_URI='http://google.com/'

#user id = 11156533090

username = '11156533090'

#erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

spotifyObject = spotipy.Spotify(auth=token)


user = spotifyObject.current_user()
# print(json.dumps(user, sort_keys=True, indent=4))
# displayName = user['display_name']
# print(displayName)
# artists = spotifyObject.search('type=artist', limit = 50)
# print(json.dumps(artists, sort_keys=True, indent=4))


# --------------- Obter os artistas e toda a informação sobre eles --------------

file1 = open('artists.txt', 'r') 
Lines = file1.readlines() 
  
count = 0

# #Strips the newline character 
# for name in Lines: 
#    #get search results
#     searchResults = spotifyObject.search(name,1,0,"artist")

#     # Artist details
#     if searchResults['artists']['items']:
#         artist = searchResults['artists']['items'][0]
#         #verify artist name
#         if artist['name']:
#             artistName= artist['name']
#         else:
#             artistName= 'None'
#         #verify artist type
#         if artist['type']:
#             artistType= artist['type']
#         else:
#             artistType= 'None'

#         #verify artist Popularity
#         if artist['popularity']:
#             artistPopularity= artist['popularity']
#         else:
#             artistPopularity = 'None'

#         #verify artist Image
#         if artist['images']:
#             artistImage = artist['images'][0]['url']
#         else:
#             artistImage = 'None'
        
#         #verify artist Followers
#         if artist['followers']:
#             artistFollowers = artist['followers']['total']
#         else:
#             artistFollowers = 'None'
        
#         genres = ""
#         print(artistName)
#         print('\t Type: ' + artistType)
#         print('\t Popularity : ' + str(artistPopularity))
#         print('\t Image URL : ' + artistImage)
#         print('\t Genres:')

#         #verify artist Genres
#         if artist['genres']:
#             for gen in artist['genres']:
#                 print('\t\t'+gen)

#         print('\t Followers : ' + str(artistFollowers))
        


#         count += 1

# print('Artistas processados: ' + str(count))



# --------------- Obter os albums e toda a informação sobre eles --------------

# albums = ""
# for name in Lines:
#     searchResults = spotifyObject.search(name,1,0,"artist")
#     if searchResults['artists']['items']:
#         artist = searchResults['artists']['items'][0]
#         artistID = artist['id']

#         # Extract album data
#         albumResults = spotifyObject.artist_albums(artistID)
#         albumResults = albumResults['items']

#         for item in albumResults:
#             #get the album name
#             if item['name']:
#                 albumName = item['name']
#             else:
#                 albumName = 'None'

#             # get the album  release date
#             if item['release_date']:
#                 albumReleaseDate = item['release_date']
#             else:
#                 albumReleaseDate = 'None'

#             # get the album total tracks
#             if item['total_tracks']:
#                 albumTotalTracks = item['total_tracks']
#             else:
#                 albumTotalTracks = 'None'

#             print('Name: ' + albumName)
#             print('\tRelease date :'+ albumReleaseDate)
#             print('\tTotal tracks: ' + str(albumTotalTracks))

#             print('\tArtists:')
#             # get the album artists
#             if item['artists']:
#                 for artist in item['artists']:
#                     artistName = artist['name']
#                     print('\t\tName: '+ artistName)

#             if item['id']:
#                 albumID = item['id']
#             if item['images']:    
#                 albumArt = item['images'][0]['url']

#             albums += albumID+'\n'


# file = open("albums.txt", "w") 

# file.write(albums) 

# file.close()








file2 = open('albums.txt', 'r') 
albumIds = file2.readlines()

for albumId in albumIds:
    albumId = albumId[:-1]
    trackResults = spotifyObject.album_tracks(albumId)
    trackResults = trackResults['items']
    print(json.dumps(trackResults, sort_keys=True, indent=4))
