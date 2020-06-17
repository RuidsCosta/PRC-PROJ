<template>
  <div>
    <v-app-bar flat color="black" >
      <v-toolbar-title>
        <v-icon left color="red">mdi-music</v-icon>
        <span class="font-black red--text">UMinhoMusic</span> 
      </v-toolbar-title>
      <v-spacer></v-spacer>

      <v-btn 
        text 
        color="white"
        @click="$router.push('/artistas')" 
      >
        <span>Artistas</span>
        <v-icon right color="white">mdi-microphone-variant</v-icon>
      </v-btn>  

      <v-btn 
        text 
        color="white"
        @click="$router.push('/albuns')"  
      >
        <span>Álbuns</span>
        <v-icon right color="white">mdi-album</v-icon>
      </v-btn>

      <v-btn 
        text 
        color="white"
        @click="$router.push('/musicas')"  
      >
        <span>Músicas</span>
        <v-icon right color="white">mdi-music-circle-outline</v-icon>
      </v-btn>
    </v-app-bar>
  </div>
</template>

<style scoped>
span {
  font-family: Georgia, 'Times New Roman', Times, serif;
}

</style>

