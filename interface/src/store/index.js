import Vue from 'vue'
import Vuex from 'vuex'

import music from './music'

Vue.use(Vuex)

export default function () {
    const Store = new Vuex.Store({
        modules: {
            music
        } 
    })
    
    return Store
}

