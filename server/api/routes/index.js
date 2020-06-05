var express = require('express');
var router = express.Router();
var spotify = require('../controllers/spotify')

router.get('/musicas', function(req, res){

    spotify.getMusicas()
        .then(dados => res.jsonp(dados))
        .catch(e => res.status(500).send(`Erro na listagem de músicas: ${e}.`))

});

module.exports = router;
