<template>
  <v-app id="artistaID">
    <Navbar />
    <v-content>
      <v-container fluid style="padding: 0%">
        <v-row id="img">
          <v-col cols="auto">
            <v-img height="250" width="250" :src="`${ artistaID.imagem }`"></v-img>
          </v-col>
          <v-col cols="auto" class="text-left pl-10 mt-n6">
            <v-row class="flex-column ma-0 fill-height" justify="center">
              <v-col class="px-0">
                <h1>{{ artistaID.artista }}</h1>
              </v-col>
              <v-col class="px-0">
                <h3>Gêneros: {{ artistaID.generos }}</h3>
              </v-col>
              <v-col class="px-0">
                <h3>Popularidade: {{ artistaID.popularidade }}</h3>
              </v-col>
              <v-col class="px-0">
                <h3>Seguidores: {{ artistaID.seguidores }}</h3>
              </v-col>
              <v-col class="px-0">
                <v-btn small rounded color="white" @click="goToSpotify(artistaID.spotify)">
                  <v-icon left color="green">mdi-spotify</v-icon>
                    <span class="green--text">Spotify</span>
                  </v-btn>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-container>
      <v-container fluid>
        <h3>Álbuns</h3>
        <hr />
        <v-container fluid style="padding: 0%">
          <v-row>
            <v-col v-for="i in albunsID" :key="i.id_album" class="child-flex" cols="auto">
              <v-card class="d-inline-block" max-width="190" @click="goToAlbum(i.id_album)">
                <v-img height="190" width="190" :src="`${ i.capa }`"></v-img>
                <h4 class="mt-2">{{ i.album }}</h4>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import Navbar from "../components/Navbar";
import { mapActions, mapState } from "vuex";

export default {
  name: "artistaID",
  components: {
    Navbar
  },
  mounted() {
    this.ActionLoadPageArtistaID(this.$route.params.id);
  },
  computed: {
    ...mapState("music", ["albunsID", "artistaID"])
  },
  methods: {
    ...mapActions("music", ["ActionLoadPageArtistaID"]),
    goToAlbum(item) {
      this.$router.push(`/albuns/${item}`)
    },
    goToSpotify(item) {
      window.open(item);
    }
  }
};
</script>

<style scoped>
#artistaID {
  background-color: black;
}

#img {
  margin-left: 90px;
}

.v-card {
  background-color: black;
  cursor: pointer;
}

h1 {
  font-size: 2.5em;
  color: white;  
  font-family: Georgia, "Times New Roman", Times, serif;  
}

h3,
h4 {
  color: white;  
  font-family: Georgia, "Times New Roman", Times, serif;
}

hr {
    border: 1px solid red;
}
</style>