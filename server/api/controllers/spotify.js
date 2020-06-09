var spotify = module.exports
const axios = require('axios')

function normalize(response) {
    return response.results.bindings.map(obj =>
        Object.entries(obj)
            .reduce((new_obj, [k,v]) => (new_obj[k] = v.value, new_obj),
                    new Object()));
}

function myNormalize(r){
    return r.results.bindings.map(o => {
        var novo = {}
        for (let [k, v] of Object.entries(o)) {
            novo[k] = v.value
          }
        return novo  
    })
}

var prefixes = `
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX noInferences: <http://www.ontotext.com/explicit>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX s: <http://www.semanticweb.org/ricardo/ontologies/2020/3/spotify#>
`

var getLink = 'http://localhost:7200/repositories/spotify' + '?query='

spotify.getMusicas = async function(){

    var query = `
    select ?id_musica ?musica ?duracao ?explicita ?id_album ?album ?id_artista ?artista ?spotify where{
    
        ?m a s:musica.
    	?m s:id ?id_musica.
        ?m s:título ?musica.
        ?m s:duracao ?duracao.
        ?m s:explicita ?explicita.
        ?m s:estáInseridaEm ?a.
    	?a s:id ?id_album.
        ?a s:título ?album.
        ?a s:éProduzidoPor ?c.
    	?c s:id ?id_artista.
        ?c s:nome ?artista.
        ?m s:spotify ?spotify.
        
    } order by (?musica) `

    var encoded = encodeURIComponent(prefixes + query)

    try{
        var response = await axios.get(getLink + encoded)
        return myNormalize(response.data)
    }
    catch(e){
        throw(e)
    }
}

spotify.getMusica = async function(idMusica){

    var query = `
    select ?musica ?duracao ?explicita ?id_album ?album ?id_artista ?artista ?spotify where{
    
    	?m s:id "${idMusica}".
        ?m s:título ?musica.
        ?m s:duracao ?duracao.
        ?m s:explicita ?explicita.
        ?m s:estáInseridaEm ?a.
    	?a s:id ?id_album.
        ?a s:título ?album.
        ?a s:éProduzidoPor ?c.
    	?c s:id ?id_artista.
        ?c s:nome ?artista.
        ?m s:spotify ?spotify.
        
    } `

    var encoded = encodeURIComponent(prefixes + query)

    try{
        var response = await axios.get(getLink + encoded)
        return myNormalize(response.data)
    }
    catch(e){
        throw(e)
    }
}

spotify.getArtistas = async function(){

    var query = `
    select ?id_artista ?artista ?seguidores ?popularidade ?generos ?imagem ?spotify where{
    
        ?a a s:artista.
    	?a s:id ?id_artista.
        ?a s:nome ?artista.
        ?a s:seguidores ?seguidores.
        ?a s:popularidade ?popularidade.
        ?a s:generos ?generos.
        ?a s:imagem ?imagem.
        ?a s:spotify ?spotify.
        
    } order by desc (?popularidade) `

    var encoded = encodeURIComponent(prefixes + query)

    try{
        var response = await axios.get(getLink + encoded)
        return myNormalize(response.data)
    }
    catch(e){
        throw(e)
    }
}

spotify.getArtista = async function(idArtista){

    var query = `
    select ?artista ?seguidores ?popularidade ?generos ?imagem ?spotify where{
    
    	?a s:id "${idArtista}".
        ?a s:nome ?artista.
        ?a s:seguidores ?seguidores.
        ?a s:popularidade ?popularidade.
        ?a s:generos ?generos.
        ?a s:imagem ?imagem.
        ?a s:spotify ?spotify.
        
    } `

    var encoded = encodeURIComponent(prefixes + query)

    try{
        var response = await axios.get(getLink + encoded)
        return myNormalize(response.data)
    }
    catch(e){
        throw(e)
    }
}

spotify.getAlbums = async function(){

    var query = `
    select ?id_album ?album ?data_lancamento ?capa ?id_artista ?artista ?spotify where{
    
        ?a a s:album.
    	?a s:id ?id_album.
        ?a s:título ?album.
        ?a s:data_lancamento ?data_lancamento.
        ?a s:capa ?capa.
        ?a s:éProduzidoPor ?art.
    	?art s:id ?id_artista.
        ?art s:nome ?artista.
        ?a s:spotify ?spotify.
        
    } order by (?album) `

    var encoded = encodeURIComponent(prefixes + query)

    try{
        var response = await axios.get(getLink + encoded)
        return myNormalize(response.data)
    }
    catch(e){
        throw(e)
    }
}

spotify.getAlbum = async function(idAlbum){

    var query = `
    select ?album ?data_lancamento ?capa ?id_artista ?artista ?spotify where{
    
    	?a s:id "${idAlbum}".
        ?a s:título ?album.
        ?a s:data_lancamento ?data_lancamento.
        ?a s:capa ?capa.
        ?a s:éProduzidoPor ?art.
    	?art s:id ?id_artista.
        ?art s:nome ?artista.
        ?a s:spotify ?spotify.
        
    } `

    var encoded = encodeURIComponent(prefixes + query)

    try{
        var response = await axios.get(getLink + encoded)
        return myNormalize(response.data)
    }
    catch(e){
        throw(e)
    }
}

spotify.getAlbumsPorArtista= async function(idArtista){

    var query = `
    select ?id_album ?album ?data_lancamento ?capa ?spotify where{
    
    	?artista s:id "${idArtista}".
    	?a s:éProduzidoPor ?artista.
    	?a s:id ?id_album.
        ?a s:título ?album.
        ?a s:data_lancamento ?data_lancamento.
        ?a s:capa ?capa.
        ?a s:spotify ?spotify.
        
    } order by (?album) `

    var encoded = encodeURIComponent(prefixes + query)

    try{
        var response = await axios.get(getLink + encoded)
        return myNormalize(response.data)
    }
    catch(e){
        throw(e)
    }
}

spotify.getMusicasPorAlbum = async function(idAlbum){

    var query = `
    select ?id_musica ?musica ?duracao ?explicita ?spotify where{
    
    	?album s:id "${idAlbum}".
    	?m s:estáInseridaEm ?album.
    	?m s:id ?id_musica.
        ?m s:título ?musica.
        ?m s:duracao ?duracao.
        ?m s:explicita ?explicita.
        ?m s:spotify ?spotify.
        
    } order by (?musica) `

    var encoded = encodeURIComponent(prefixes + query)

    try{
        var response = await axios.get(getLink + encoded)
        return myNormalize(response.data)
    }
    catch(e){
        throw(e)
    }
}