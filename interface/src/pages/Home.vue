<template>
    <v-app id="home">
        <Navbar />
        <v-content>
            <v-container fluid style="padding: 0%">
                <v-img src="../assets/topo.png" height="210px">
                    <div>
                        <p style="color:white">Teste</p>
                    </div>
                </v-img>    
            </v-container>
        </v-content>
    </v-app>    
</template>

<script>
import Navbar from '../components/Navbar'

export default {
    name: 'home',
    components: {
        Navbar
    }
}
</script>


<style scoped>

</style>