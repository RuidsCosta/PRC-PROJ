<template>
  <v-app id="musicas">
    <Navbar />
    <v-content>
      <v-container fluid>
        <h3>Músicas</h3>
        <hr />
        <v-container fluid>
          <v-card>
            <v-card-title>
              <v-text-field
                v-model="search"
                append-icon="mdi-magnify"
                label="Pesquisar"
                single-line
                hide-details
              ></v-text-field>
            </v-card-title>
            <v-data-table id="table" :headers="headers" :items="musicas" :search="search">
              <template v-slot:no-data>
                <v-data-table id="table" hide-default-footer loading loading-text="A carregar... Por favor espere"></v-data-table>
              </template>
              <template v-slot:item="row">
                <tr>
                  <td>{{row.item.musica}}</td>
                  <td>{{row.item.artista}}</td>
                  <td>{{row.item.album}}</td>
                  <td>{{verifyExplicit(row.item.explicita)}}</td>
                  <td>{{millisToMinutesAndSeconds(row.item.duracao)}}</td>
                  <td>
                    <v-btn small rounded color="black" @click="goToSpotify(row.item.spotify)">
                      <v-icon left color="green">mdi-spotify</v-icon>
                      <span class="white--text">Spotify</span>
                    </v-btn>
                  </td>
                </tr>
            </template>
            </v-data-table>
          </v-card>
        </v-container>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import Navbar from "../components/Navbar";
import { mapActions, mapState } from "vuex";

export default {
  name: "musicas",
  components: {
    Navbar
  },
  data: () => ({
    search: "",
    headers: [
      { text: "Música", width:"25%", sortable: true, value: "musica", class: "overline red--text" },
      { text: "Artista", width:"25%", sortable: true, value: "artista", class: "overline red--text" },
      { text: "Álbum", width:"25%", sortable: true, value: "album", class: "overline red--text" },
      { text: "", sortable: true, value: "explicita", class: "overline red--text" },
      { text: "Duração", sortable: false, value: "duracao", class: "overline red--text" }
    ]
  }),
  mounted() {
    this.ActionLoadPageMusicas();
  },
  computed: {
    ...mapState("music", ["musicas"])
  },
  methods: {
    ...mapActions("music", ["ActionLoadPageMusicas"]),
    goToSpotify(item) {
      window.open(item);
    },
    verifyExplicit(item) {
      if (item == "True") {
        return "Explícita"
      }
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
#musicas {
  background-color: black;
}

#table {
  font-family: Georgia, 'Times New Roman', Times, serif;
}

h3 {
  margin-left: 10px;
  color: white;
  font-family: Georgia, 'Times New Roman', Times, serif;
}

hr {
  margin-left: 10px;
  margin-right: 10px;
  border: 1px solid red;
}
</style>