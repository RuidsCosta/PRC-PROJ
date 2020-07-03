<template>
  <v-app id="artistas">
    <Navbar />
    <v-content>
      <v-container fluid>
        <h3>Artistas</h3>
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
            <v-data-table id="table" :headers="headers" :items="artistas" :search="search">
              <template v-slot:no-data>
                <v-data-table id="table" hide-default-footer loading loading-text="A carregar... Por favor espere"></v-data-table>
              </template>
              <template v-slot:item="row">
                <tr @click="goToArtist(row.item.id_artista)">
                  <td>{{row.item.artista}}</td>
                  <td>{{row.item.generos}}</td>
                  <td>{{row.item.popularidade}}</td>
                  <td>{{row.item.seguidores}}</td>
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
  name: "artistas",
  components: {
    Navbar
  },
  data: () => ({
    search: '',
    headers: [
      { text: "Artista", width:"20%", sortable: true, value: "artista", class: "overline red--text" },
      { text: "Gênero", width:"45%", sortable: false, value: "generos", class: "overline red--text" },
      { text: "Popularidade", sortable: true, value: "popularidade", class: "overline red--text" },
      { text: "Seguidores", sortable: true, value: "seguidores", class: "overline red--text" }
    ]
  }),
  mounted() {
    this.ActionLoadPageArtistas();
  },
  computed: {
    ...mapState("music", ["artistas"])
  },
  methods: {
    ...mapActions("music", ["ActionLoadPageArtistas"]),
    goToArtist(item) {
      this.$router.push(`/artistas/${item}`)
    },
    goToSpotify(item) {
      window.open(item);
    }
  }
};
</script>

<style scoped>
#artistas {
  background-color: black;
}

#table {
  font-family: Georgia, 'Times New Roman', Times, serif;
  cursor: pointer;
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