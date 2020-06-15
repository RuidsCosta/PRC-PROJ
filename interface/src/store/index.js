import Vue from 'vue'
import Vuex from 'vuex'

import spotify from './spotify'

Vue.use(Vuex)

export default function () {
    const Store = new Vuex.Store({
        modules: {
            spotify
        } 
    })
    
    return Store
}

