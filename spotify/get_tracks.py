#!/usr/bin/python3

import sys
import spotipy
import spotipy.util as util
import csv

def get_all_albums():

    print('    get_all_albums()')

    albums = []

    with open('albums.csv') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader, None)

        for row in csv_reader:
            albums.append(row[0])

    return albums

def get_tracks_by_album(token, albums):

    print('    get_tracks_by_artist()')

    if token:

        print('        Token accepted!')

        tracks_csv = open('tracks.csv', mode='w')
        number_tracks = 0

        sp = spotipy.Spotify(auth=token)

        with tracks_csv as csv_file:

            field_names = ['id', 'nome', 'album', 'duracao', 'explicita', 'spotify']
            writer = csv.DictWriter(csv_file, fieldnames=field_names, delimiter =';')
            writer.writeheader()

            print('        Parsing tracks...')

            for album in albums:

                items = sp.album_tracks(album, limit=50, offset=0)

                for track in items['items']:

                    writer.writerow({'id':track['id'], 
                                     'nome':track['name'], 
                                     'album':album, 
                                     'duracao':track['duration_ms'], 
                                     'explicita':track['explicit'], 
                                     'spotify':track['external_urls']['spotify']})
                    number_tracks += 1

        tracks_csv.close()

        print(f'        Parsed {number_tracks} tracks!')

        return number_tracks
        

    else:
        print("        Can't get token for", username)
        return 0

if __name__ == '__main__':

    print('get_tracks()')

    username = '31rky7r2l7h5eqvp42hbhnxm2ymm'
    scope = ''

    token = util.prompt_for_user_token(username,
                                    scope,
                                    client_id = 'f414bbb0e9c445a2a08b5d734a577680',
                                    client_secret = '331a8fa7068a4725b65b6af97ca47bc0',
                                    redirect_uri = 'http://localhost')

    albums = get_all_albums()

    get_tracks_by_album(token, albums)