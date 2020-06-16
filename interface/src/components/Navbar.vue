<template>
  <div>
    <v-app-bar flat color="black" >
      <v-toolbar-title>
        <v-icon left color="red">mdi-music</v-icon>
        <span class="title font-black red--text">UMinhoMusic</span> 
      </v-toolbar-title>
      <v-spacer></v-spacer>

      <v-btn 
        text 
        color="white"
        @click="$router.push('/artistas')" 
        class="font-weight-light"
      >
        <span>Artistas</span>
        <v-icon right color="white">mdi-microphone-variant</v-icon>
      </v-btn>  

      <v-btn 
        text 
        color="white"
        @click="$router.push('/albuns')"  
        class="font-weight-light"
      >
        <span>Álbuns</span>
        <v-icon right color="white">mdi-album</v-icon>
      </v-btn>

      <v-btn 
        text 
        color="white"
        @click="$router.push('/musicas')"  
        class="font-weight-light"
      >
        <span>Músicas</span>
        <v-icon right color="white">mdi-music-circle-outline</v-icon>
      </v-btn>
    </v-app-bar>
  </div>
</template>

