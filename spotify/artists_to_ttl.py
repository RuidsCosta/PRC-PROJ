#!/usr/bin/python3

import csv

'''
###  http://www.semanticweb.org/ricardo/ontologies/2020/3/spotify#artista1
:artista1 rdf:type owl:NamedIndividual ,
                   :artista ;
          :generos "rock, metal rock"^^xsd:string ;
          :imagem "http://imgur.com/artista1"^^xsd:string ;
          :nome "artista1"^^xsd:string ;
          :popularidade "72"^^xsd:int ;
          :seguidores "52400"^^xsd:int ;
          :spotify "http://spotify.com/artista1"^^xsd:string .
'''

if __name__ == '__main__':

    print('artists_to_ttl()')

    artists_csv = open('artists.csv')
    artists_ttl = open('artists.ttl', 'w')
    print('    Artists.csv opened!')


    print('    Copying artists...')
    with artists_csv as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=';')
        iterreader = iter(csv_reader)
        next(iterreader)
        for row in iterreader:

            id = row[0]
            nome = str(row[1]).replace('\"', '')
            popularidade = row[2]
            seguidores = row[3]
            generos = row[4]
            spotify = row[5]
            imagem = row[6]

            artists_ttl.write(f'###  http://www.semanticweb.org/ricardo/ontologies/2020/3/spotify#{id}\n')
            artists_ttl.write(f':{id} rdf:type owl:NamedIndividual ,\n')
            artists_ttl.write(f'        :artista ;\n')
            artists_ttl.write(f'    :generos "{generos}"^^xsd:string ;\n')
            artists_ttl.write(f'    :imagem "{imagem}"^^xsd:string ;\n')
            artists_ttl.write(f'    :nome "{nome}"^^xsd:string ;\n')
            artists_ttl.write(f'    :popularidade "{popularidade}"^^xsd:int ;\n')
            artists_ttl.write(f'    :seguidores "{seguidores}"^^xsd:int ;\n')
            artists_ttl.write(f'    :spotify "{spotify}"^^xsd:string .\n')
            artists_ttl.write('\n\n')

    artists_csv.close()
    artists_ttl.close()
    print('    Files closed!')