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


artists = ""
line_count = 0
#read the name file 1
with open('artists1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count1 = 0
    for row in csv_reader:
        if line_count1 == 0:
            line_count1 += 1
            line_count += 1
        else:
            # print(f'\tArtist name: {row[0]}.')
            line_count += 1
            artists+=row[0]+'\n'

#read the name file 2
with open('artists2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count2 = 0
    for row in csv_reader:
        if line_count2 == 0:
            line_count2 += 1
            line_count += 1
        else:
            # print(f'\tArtist name: {row[0]}.')
            line_count += 1
            artists+=row[0]+'\n'

#read the name file 3
with open('artists3.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count3 = 0
    for row in csv_reader:
        if line_count3 == 0:
            line_count3 += 1
            line_count += 1
        else:
            # print(f'\tArtist name: {row[0]}.')
            line_count += 1
            artists+=row[0]+'\n'

#read the name file 4
with open('artists4.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count4 = 0
    for row in csv_reader:
        if line_count4 == 0:
            line_count4 += 1
            line_count += 1
        else:
            # print(f'\tArtist name: {row[0]}.')
            line_count += 1
            artists+=row[0]+'\n'

file = open("artists.txt", "w") 

file.write(artists) 

file.close()
print(f'Processed {line_count} lines.')


    

