export default {
    SET_ARTISTAS (state, payload) {
        state.artistas = payload
    },
    SET_ARTISTA_ID (state, payload) {
        state.artistaID = payload
    },
    SET_ALBUNS (state, payload) {
        state.albuns = payload
    },
    SET_ALBUNS_ID (state, payload) {
        state.albunsID = payload
    },
    SET_MUSICAS (state, payload) {
        state.musicas = payload
    },
    SET_MUSICAS_ALBUM (state, payload) {
        state.musicasAlbum = payload
    }  
}