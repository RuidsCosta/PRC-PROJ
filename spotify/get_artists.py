#!/usr/bin/python3

import sys
import spotipy
import spotipy.util as util
import csv
import pandas as pd

def get_top_artists(token):

    print('    get_top_artists()')

    if token:

        print('        Token accepted!')

        artists_csv = open('artists.csv', mode='w')
        number_artists = 0

        sp = spotipy.Spotify(auth=token)
        
        with artists_csv as csv_file:

            field_names = ['id', 'nome', 'popularidade', 'seguidores', 'genero', 'spotify', 'imagem']
            writer = csv.DictWriter(csv_file, fieldnames=field_names, delimiter =';')
            writer.writeheader()

            print('        Parsing artists...')

            items = sp.current_user_top_artists(limit=49, offset=0)
            for artist in items['items']:

                genres = str(artist['genres']).replace('\'', '').replace('[', '').replace(']', '')

                writer.writerow({'id':artist['id'], 
                                 'nome':artist['name'], 
                                 'popularidade':artist['popularity'], 
                                 'seguidores':artist['followers']['total'], 
                                 'genero':genres, 
                                 'spotify':artist['external_urls']['spotify'], 
                                 'imagem':artist['images'][0]['url']})
                number_artists += 1

            items = sp.current_user_top_artists(limit=39, offset=49)
            for artist in items['items']:

                genres = str(artist['genres']).replace('\'', '').replace('[', '').replace(']', '')

                writer.writerow({'id':artist['id'], 
                                 'nome':artist['name'], 
                                 'popularidade':artist['popularity'], 
                                 'seguidores':artist['followers']['total'], 
                                 'genero':genres, 
                                 'spotify':artist['external_urls']['spotify'], 
                                 'imagem':artist['images'][0]['url']})
                number_artists += 1

        artists_csv.close()

        print(f'        Parsed {number_artists} artists!')
        return number_artists

    else:
        print("        Can't get token for", username)
        return 0

def get_related_artists(token, number_artists):

    print('    get_related_artists()')

    if token:

        print('        Token accepted!')

        artists_csv_read = open('artists.csv', mode='r')
        artists_csv_append = open('artists.csv', mode='a')
        more_artists = 0

        sp = spotipy.Spotify(auth=token)
        
        with artists_csv_append as csv_file:

            field_names = ['id', 'nome', 'popularidade', 'seguidores', 'genero', 'spotify', 'imagem']
            reader = csv.reader(artists_csv_read, delimiter=';')
            iterreader = iter(reader)
            next(iterreader)
            appender = csv.DictWriter(csv_file, fieldnames=field_names, delimiter =';')

            print('        Parsing related artists...')

            flag = 0
            for row in iterreader:

                if flag >= number_artists:
                    break
                else:
                    
                    id_artist = row[0]

                    items = sp.artist_related_artists(id_artist)
                    for artist in items['artists']:

                        if artist['genres'] != [] and artist['images'] != []:

                            genres = str(artist['genres']).replace('\'', '').replace('[', '').replace(']', '')

                            appender.writerow({'id':artist['id'], 
                                            'nome':artist['name'], 
                                            'popularidade':artist['popularity'], 
                                            'seguidores':artist['followers']['total'], 
                                            'genero':genres, 
                                            'spotify':artist['external_urls']['spotify'], 
                                            'imagem':artist['images'][0]['url']})

                            more_artists += 1
                    flag += 1

        artists_csv_read.close()
        artists_csv_append.close()

        print(f'        Appended {more_artists} more artists!')
        print('        CAUTION: may have duplicates...')

        return more_artists

    else:
        print("        Can't get token for", username)
        return 0

def normalize_csv():

    print('    normalize_csv()')

    data = pd.read_csv("artists.csv", sep=';') 

    data.sort_values("popularidade", inplace = True, ascending=False) 
    print('        Artists sorted!')

    data.drop_duplicates(subset = 'id', inplace = True, keep = 'first')
    print('        Duplicates removed!')

    data.to_csv('artists.csv', index = False, sep=';')
    print('        Normalized!')


if __name__ == '__main__':

    print('get_artists()')

    username = '31rky7r2l7h5eqvp42hbhnxm2ymm'
    scope = 'user-top-read'

    token = util.prompt_for_user_token(username,
                                    scope,
                                    client_id = 'f414bbb0e9c445a2a08b5d734a577680',
                                    client_secret = '331a8fa7068a4725b65b6af97ca47bc0',
                                    redirect_uri = 'http://localhost')

    number_artists = get_top_artists(token)

    more_artists = get_related_artists(token, number_artists)
    print(f'    Parsed a total of {number_artists+more_artists} artists!')

    normalize_csv()