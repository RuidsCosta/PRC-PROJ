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
    }
]