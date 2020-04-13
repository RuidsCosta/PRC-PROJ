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
# escreve os ids dos artistas no artists-txt para depois, apartir de todos os ids irmos buscar as informaçoes
# dos albums e musicas

file1 = open('artists.txt', 'r') 
Lines = file1.readlines() 
  
# count = 0
# artistForm = ""
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
#         if artist['id']:
#             artistID= artist['id']
#         else:
#             artistID= 'None'

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
        
            
#         genres = ""
    


#         artistForm += (f'###  http://www.semanticweb.org/ricardo/ontologies/2020/3/spotify#{artistID}\n')
#         artistForm += (f':{artistID} rdf:type owl:NamedIndividual ,\n')
#         artistForm += (f'\t:artista ;\n')
        
#         #verify artist Genres
#         gencount = 0
#         if artist['genres']:
#             artistForm += (f'\t:gênero ')
#             for gen in artist['genres']:
#                 if gencount == 0:
#                     artistForm += (f'"{gen}"^^xsd:string ,\n')
#                 elif gencount == len(artist['genres'])-1:
#                     artistForm += (f'\t\t"{gen}"^^xsd:string ;\n')
#                 else:
#                     artistForm += (f'\t\t"{gen}"^^xsd:string ,\n')
#                 gencount += 1

#         artistForm += (f'\t:nome "{artistName}"^^xsd:string ;\n')

#         if artist['followers']:
#             artistFollowers = artist['followers']['total']
#             artistForm += (f'\t:seguidores "{artistFollowers}"^^xsd:long .\n')
#         else:
#             artistFollowers = 'None'
#         artistForm += ('\n\n\n')

#         count += 1
#         print('artistas processados: '+str(count))
# print('Artistas processados: ' + str(count))

# file = open("artitsts_formatted.ttl", "w") 

# file.write(artistForm) 

# file.close()


# --------------- Obter os albums e toda a informação sobre eles --------------




# albcount = 0
# albums = ""
# albumForm = ""
# for name in Lines:
#     searchResults = spotifyObject.search(name,1,0,"artist")
#     if searchResults['artists']['items']:
#         artist = searchResults['artists']['items'][0]
#         artistID = artist['id']

#         # Extract album data
#         albumResults = spotifyObject.artist_albums(artistID)
#         albumResults = albumResults['items']

#         for item in albumResults:
            

           

#             # get the album total tracks
#             if item['total_tracks']:
#                 albumTotalTracks = item['total_tracks']
#             else:
#                 albumTotalTracks = 'None'
            

            
            

#             if item['id']:
#                 albumID = item['id']
#             if item['images']:    
#                 albumArt = item['images'][0]['url']




#             albumForm += (f'###  http://www.semanticweb.org/ricardo/ontologies/2020/3/spotify#{albumID}\n')
#             albumForm += (f':{albumID} rdf:type owl:NamedIndividual ,\n')
#             albumForm += (f'\t\t:álbum ;\n')
#             artistCount = 0
#             # get the album artists
#             if item['artists']:
#                 albumForm += (f'\t:éProduzidoPor')
#                 for artist in item['artists']:
#                     artistNames = artist['name']
#                     if artistCount == 0:
#                         albumForm += (f'\t\t:{artistNames} ,\n')
#                     elif artistCount == len(item['artists'])-1:
#                         albumForm += (f'\t\t:{artistNames} ;\n')
#                     else:
#                         albumForm += (f'\t\t:{artistNames} ,\n')
#                     artistCount += 1
#                      # get the album  release date
#             if item['release_date']:
#                 albumReleaseDate = item['release_date']
#                 albumForm += (f'\t:dataLançamento "{albumReleaseDate}"^^xsd:string ;\n')
#             else:
#                 albumReleaseDate = 'None'
            

#             #get the album name
#             if item['name']:
#                 albumName = item['name']
#                 albumForm += (f'\t:designação "{albumName}"^^xsd:string .')

#             else:
#                 albumName = 'None'
#             albumForm += (f'\n\n\n')

#             albums += albumID+'\n'
#             albcount+=1
#             print ("albums processados: "+ str(albcount))


# file = open("albums.txt", "w") 

# file.write(albums) 

# file.close()


# file = open("albums_formatted.ttl", "w") 

# file.write(albumForm) 

# file.close()






musicForm = ""
musicCount = 0
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
                    
    musicCount += 1
    print('Artista nr: ' + str(musicCount))





file = open("musics_formatted.ttl", "w") 

file.write(musicForm) 

file.close()

















        

