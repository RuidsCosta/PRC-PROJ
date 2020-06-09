#!/usr/bin/python3

import csv

'''
###  http://www.semanticweb.org/ricardo/ontologies/2020/3/spotify#musica1
:musica1 rdf:type owl:NamedIndividual ,
                  :musica ;
         :duracao "240"^^xsd:int ;
         :id "musica1"^^xsd:string ;
         :explicita "True"^^xsd:string ;
         :spotify "http://spotify.com/musica1"^^xsd:string ;
         :título "musica1"^^xsd:string .
'''

if __name__ == '__main__':

    print('tracks_to_ttl()')

    musicas_csv = open('tracks.csv')
    musicas_ttl = open('tracks.ttl', 'w')
    print('    tracks.csv opened!')


    print('    Copying tracks...')
    with musicas_csv as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=';')
        iterreader = iter(csv_reader)
        next(iterreader)
        for row in iterreader:

            id = row[0]
            nome = str(row[1]).replace('\"', '')
            album = row[2]
            duracao = row[3]
            explicita = row[4]
            spotify = row[5]

            musicas_ttl.write(f'###  http://www.semanticweb.org/ricardo/ontologies/2020/3/spotify#{id}\n')
            musicas_ttl.write(f':{id} rdf:type owl:NamedIndividual ,\n')
            musicas_ttl.write(f'        :musica ;\n')
            musicas_ttl.write(f'    :estáInseridaEm :{album} ;\n')
            musicas_ttl.write(f'    :duracao "{duracao}"^^xsd:int ;\n')
            musicas_ttl.write(f'    :explicita "{explicita}"^^xsd:string ;\n')
            musicas_ttl.write(f'    :spotify "{spotify}"^^xsd:string ;\n')
            musicas_ttl.write(f'    :título "{nome}"^^xsd:string ;\n')
            musicas_ttl.write(f'    :id "{id}"^^xsd:string .\n')
            musicas_ttl.write('\n\n')

    musicas_csv.close()
    musicas_ttl.close()
    print('    Files closed!')