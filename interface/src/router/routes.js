export default [
    {
        path: '/',
        name: 'home',
        component: () => import('../pages/Home')
    },
    {
        path: '/artistas',
        name: 'artistas',
        component: () => import('../pages/Artistas')
    },
    {
        path: '/artistas/:id',
        name: 'artistaID',
        component: () => import('../pages/ArtistaID')
    },
    {
        path: '/albuns',
        name: 'albuns',
        component: () => import('../pages/Albuns')
    },
    {
        path: '/albuns/:id',
        name: 'albumID',
        component: () => import('../pages/AlbumID')
    },
    {
        path: '/musicas',
        name: 'musicas',
        component: () => import('../pages/Musicas')
    }
]