import services from '@/http'

export const ActionLoadPageHome = ({ commit }) => {
    services.http.loadArtistas().then(res => {
        commit('SET_ARTISTAS', res.data)
    }),
    services.http.loadAlbuns().then(res => {
        commit('SET_ALBUNS', res.data)
    }),
    services.http.loadMusicas().then(res => {
        commit('SET_MUSICAS', res.data)
    })
}

export const ActionLoadPageArtistas = ({ commit }) => {
    services.http.loadArtistas().then(res => {
        commit('SET_ARTISTAS', res.data)
    })
} 