export default {
    http: {
        loadArtistas: { method: 'get', url: 'artistas' },
        loadArtistaID: { method: 'get', url: 'artistas{/id}' },
        loadArtistaAlbuns: { method: 'get', url: 'albumsPorArtista{/id}' },
        loadAlbuns: { method: 'get', url: 'albums'},
        loadAlbumID: { method: 'get', url: 'albums{/id}' },
        loadMusicasAlbum: { method: 'get', url: 'musicasPorAlbum{/id}' },
        loadMusicas: { method: 'get', url: 'musicas'}
    }
}