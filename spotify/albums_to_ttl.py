#!/usr/bin/python3

import csv

'''
###  http://www.semanticweb.org/ricardo/ontologies/2020/3/spotify#album1
:album1 rdf:type owl:NamedIndividual ,
                 :album ;
        :éProduzidoPor :artista1 ;
        :capa "htpp://imgur.com/capa1"^^xsd:string ;
        :data_lancamento "2019-05-12"^^xsd:string ;
        :spotify "http://spotify.com/album1"^^xsd:string ;
        :título "Album1"^^xsd:string .
'''

if __name__ == '__main__':

    print('albums_to_ttl()')

    albums_csv = open('albums.csv')
    albums_ttl = open('albums.ttl', 'w')
    print('    albums.csv opened!')


    print('    Copying albums...')
    with albums_csv as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=';')
        iterreader = iter(csv_reader)
        next(iterreader)
        for row in iterreader:

            id = row[0]
            nome = str(row[1]).replace('\"', '')
            artista = row[2]
            total_musicas = row[3]
            data_lancamento = row[4]
            spotify = row[5]
            imagem = row[6]

            albums_ttl.write(f'###  http://www.semanticweb.org/ricardo/ontologies/2020/3/spotify#{id}\n')
            albums_ttl.write(f':{id} rdf:type owl:NamedIndividual ,\n')
            albums_ttl.write(f'        :album ;\n')
            albums_ttl.write(f'    :éProduzidoPor :{artista} ;\n')
            albums_ttl.write(f'    :capa "{imagem}"^^xsd:string ;\n')
            albums_ttl.write(f'    :data_lancamento "{data_lancamento}"^^xsd:string ;\n')
            albums_ttl.write(f'    :spotify "{spotify}"^^xsd:string ;\n')
            albums_ttl.write(f'    :título "{nome}"^^xsd:string .\n')
            albums_ttl.write('\n\n')

    albums_csv.close()
    albums_ttl.close()
    print('    Files closed!')