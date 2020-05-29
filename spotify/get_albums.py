#!/usr/bin/python3

import sys
import spotipy
import spotipy.util as util
import csv

def get_all_artists():

    print('    get_all_artists()')

    artists = []

    with open('artists.csv') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader, None)

        for row in csv_reader:
            artists.append(row[0])

    return artists

def get_albums_by_artist(token, artists):

    print('    get_albums_by_artist()')

    if token:

        print('        Token accepted!')

        albums_csv = open('albums.csv', mode='w')
        number_albums = 0

        sp = spotipy.Spotify(auth=token)

        with albums_csv as csv_file:

            field_names = ['id', 'nome', 'artista', 'total_musicas', 'data_lancamento', 'spotify', 'imagem']
            writer = csv.DictWriter(csv_file, fieldnames=field_names, delimiter =';')
            writer.writeheader()

            print('        Parsing albums...')

            for artist in artists:

                items = sp.artist_albums(artist, album_type='album', country='PT', limit=50, offset=0)

                for album in items['items']:

                    if album['images'] != []:

                        writer.writerow({'id':album['id'], 
                                        'nome':album['name'], 
                                        'artista':artist, 
                                        'total_musicas':album['total_tracks'], 
                                        'data_lancamento':album['release_date'], 
                                        'spotify':album['external_urls']['spotify'], 
                                        'imagem':album['images'][0]['url']})
                        number_albums += 1

        albums_csv.close()

        print(f'        Parsed {number_albums} albums!')

        return number_albums
        

    else:
        print("        Can't get token for", username)
        return 0

if __name__ == '__main__':

    print('get_albums()')

    username = '31rky7r2l7h5eqvp42hbhnxm2ymm'
    scope = ''

    token = util.prompt_for_user_token(username,
                                    scope,
                                    client_id = 'f414bbb0e9c445a2a08b5d734a577680',
                                    client_secret = '331a8fa7068a4725b65b6af97ca47bc0',
                                    redirect_uri = 'http://localhost')

    artists = get_all_artists()

    get_albums_by_artist(token, artists)