SPOTIFY EM VUE
Processamento e Representação de Conhecimento

Executar:

    pip3 install spotipy --user
    pip3 install pandas --user
    python3 get_artists.py
    python3 get_albums.py
    python3 get_artists.py
    python3 artists_to_ttl.py
    python3 albums_to_ttl.py
    python3 tracks_to_ttl.py
    Juntar todos os .ttls ao spotify.ttl, criando a full_ontology.ttl.
    Carregar no GraphDB, com repository-name "spotify".
    Enjoy!
