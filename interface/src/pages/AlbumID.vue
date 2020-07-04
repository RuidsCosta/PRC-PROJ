<template>
  <v-app id="albumID">
    <Navbar />
    <v-content>
      <v-container fluid style="padding: 0%">
        <div id="topo"></div>
        <v-row id="img">
          <v-col cols="auto">
            <v-img height="250" width="250" :src="`${ albunsID[0].capa }`"></v-img>
          </v-col>
          <v-col cols="auto" class="text-left pl-10 mt-3">
            <v-row class="flex-column ma-0 fill-height" justify="center">
              <v-col class="px-0">
                <h1>{{ albunsID[0].album }}</h1>
              </v-col>
              <v-col class="px-0">
                <h3>{{ albunsID[0].artista }}</h3>
              </v-col>
              <v-col class="px-0 black--text">
                <h4>Data de lançamento {{ albunsID[0].data_lancamento }}</h4>
              </v-col>
              <v-col class="px-0">
                <v-btn small rounded color="black" @click="goToSpotifyAlbum(albunsID[0].spotify)">
                  <v-icon left color="green">mdi-spotify</v-icon>
                  <span class="white--text">Spotify</span>
                </v-btn>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-container>
      <v-container fluid style="padding: 0%">
        <v-simple-table id="table">
          <template v-slot:default>
            <thead>
              <tr>
                <th class="overline red--text">Faixas</th>
                <th class="overline red--text"></th>
                <th class="overline red--text">Duração</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="i in musicasAlbum" :key="i">
                <td width="50%">{{i.musica}}</td>
                <td width="15%">{{verifyExplicit(i.explicita)}}</td>
                <td width="15%">{{millisToMinutesAndSeconds(i.duracao)}}</td>
                <td>
                    <v-btn small rounded color="black" @click="goToSpotifyMusic(i.spotify)">
                      <v-icon left color="green">mdi-spotify</v-icon>
                      <span class="white--text">Spotify</span>
                    </v-btn>
                  </td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import Navbar from "../components/Navbar";
import { mapActions, mapState } from "vuex";

export default {
  name: "albumID",
  components: {
    Navbar
  },
  mounted() {
    this.ActionLoadPageAlbumID(this.$route.params.id);
  },
  computed: {
    ...mapState("music", ["albunsID", "musicasAlbum"])
  },
  methods: {
    ...mapActions("music", ["ActionLoadPageAlbumID"]),
    verifyExplicit(item) {
      if (item == "True") {
        return "Explícita";
      }
    },
    goToSpotifyAlbum(item) {
      window.open(item);
    },
    goToSpotifyMusic(item) {
      window.open(item)
    },
    millisToMinutesAndSeconds(millis) {
      var minutes = Math.floor(millis / 60000);
      var seconds = ((millis % 60000) / 1000).toFixed(0);
      return minutes + ":" + (seconds < 10 ? '0' : '') + seconds;
    }
  }
};
</script>

<style scoped>
#topo {
  width: 100%;
  height: 200px;
  background-color: #d50000;
}

#img {
  margin-top: -160px;
  margin-left: 50px;
}

#table {
  font-family: Georgia, "Times New Roman", Times, serif;
  margin-left: 60px;
  margin-right: 60px;
  margin-bottom: 40px;
}

h1 {
  font-size: 2.5em;
  color: white;
  font-family: Georgia, "Times New Roman", Times, serif;
}

h3 {
  color: white;
  font-family: Georgia, "Times New Roman", Times, serif;
}

h4 {
  color: black;
  font-family: Georgia, "Times New Roman", Times, serif;
}
</style>