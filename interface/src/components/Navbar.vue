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
        @click="$router.push('/about')" 
        class="font-weight-light"
      >
        <span>About</span>
        <v-icon right color="white">mdi-information-outline</v-icon>
      </v-btn>

      <v-btn 
        text 
        color="white"
        @click="$router.push('/team')"  
        class="font-weight-light"
      >
        <span>Team</span>
        <v-icon right color="white">mdi-account-group</v-icon>
      </v-btn>
    </v-app-bar>
  </div>
</template>