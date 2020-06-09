var express = require('express');
var router = express.Router();
var spotify = require('../controllers/spotify')

// GET todas as musicas
router.get('/musicas', function(req, res){

    spotify.getMusicas()
        .then(dados => res.jsonp(dados))
        .catch(e => res.status(500).send(`Erro na listagem de músicas: ${e}.`))

});

// GET musica por ID
router.get('/musicas/:id', function(req, res) {

    spotify.getMusica(req.params.id)
        .then(dados => res.jsonp(dados))
        .catch(e => res.status(500).send(`Erro na listagem da música ${req.params.id}: ${e}`))

});

// GET todos os artistas
router.get('/artistas', function(req, res) {

    spotify.getArtistas()
        .then(dados => res.jsonp(dados))
        .catch(e => res.status(500).send(`Erro na listagem de artistas: ${e}.`))

});

// GET artista por ID
router.get('/artistas/:id', function(req, res) {

    spotify.getArtista(req.params.id)
        .then(dados => res.jsonp(dados))
        .catch(e => res.status(500).send(`Erro na listagem do artista ${req.params.id}: ${e}`))

});

// GET todos os albums
router.get('/albums', function(req, res) {

    spotify.getAlbums()
        .then(dados => res.jsonp(dados))
        .catch(e => res.status(500).send(`Erro na listagem de albums: ${e}.`))

});

// GET album por ID
router.get('/albums/:id', function(req, res) {

    spotify.getAlbum(req.params.id)
        .then(dados => res.jsonp(dados))
        .catch(e => res.status(500).send(`Erro na listagem do album ${req.params.id}: ${e}`))

});

// GET todos os albums de um artista
router.get('/albumsPorArtista/:idArtista', function(req, res) {

    spotify.getAlbumsPorArtista(req.params.idArtista)
        .then(dados => res.jsonp(dados))
        .catch(e => res.status(500).send(`Erro na listagem de albums do artista: ${e}.`))

});

// GET todas as musicas de um album
router.get('/musicasPorAlbum/:idAlbum', function(req, res) {

    spotify.getMusicasPorAlbum(req.params.idAlbum)
        .then(dados => res.jsonp(dados))
        .catch(e => res.status(500).send(`Erro na listagem de músicas do album: ${e}.`))

});

module.exports = router;
