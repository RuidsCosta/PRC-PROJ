import services from '@/http'

export const ActionLoadPageHome = ({ commit }) => {
    services.http.loadArtistas().then(res => {
        commit('SET_ARTISTAS', res.data)
    }),
    services.http.loadAlbuns().then(res => {
        commit('SET_ALBUNS', res.data)
    })
}

export const ActionLoadPageArtistas = ({ commit }) => {
    services.http.loadArtistas().then(res => {
        commit('SET_ARTISTAS', res.data)
    })
} 

export const ActionLoadPageArtistaID = ({ commit }, payload) => {
    services.http.loadArtistaID({ id: payload }).then(res => {
        commit('SET_ARTISTA_ID', res.data[0])
    }),
    services.http.loadArtistaAlbuns({ id: payload }).then(res => {
        commit('SET_ALBUNS_ID', res.data)
    })
} 

export const ActionLoadPageAlbuns = ({ commit }) => {
    services.http.loadAlbuns().then(res => {
        commit('SET_ALBUNS', res.data)
    })
}

export const ActionLoadPageAlbumID = ({ commit }, payload) => {
    services.http.loadAlbumID({ id: payload }).then(res => {
        commit('SET_ALBUNS_ID', res.data)
    }),
    services.http.loadMusicasAlbum({ id: payload }).then(res => {
        commit('SET_MUSICAS_ALBUM', res.data)
    })
} 

export const ActionLoadPageMusicas = ({ commit }) => {
    services.http.loadMusicas().then(res => {
        commit('SET_MUSICAS', res.data)
    })
} 


