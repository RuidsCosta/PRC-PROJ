<template>
  <v-app id="albuns">
    <Navbar />
    <v-content>
      <v-container fluid>
        <h3>Álbuns</h3>
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
            <v-data-table id="table" :headers="headers" :items="albuns" :search="search">
              <template v-slot:no-data>
                <v-data-table id="table" hide-default-footer loading loading-text="A carregar... Por favor espere"></v-data-table>
              </template>
              <template v-slot:item="row">
                <tr @click="goToAlbum(row.item.id_album)">
                  <td>{{row.item.album}}</td>
                  <td>{{row.item.artista}}</td>
                  <td>{{row.item.data_lancamento}}</td>
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
  name: "albuns",
  components: {
    Navbar
  },
  data: () => ({
    search: '',
    headers: [
      { text: "Álbum", width:"40%", sortable: true, value: "album", class: "overline red--text" },
      { text: "Artista", width:"30%", sortable: true, value: "artista", class: "overline red--text" },
      { text: "Data Lançamento", width:"18%", sortable: true, value: "data_lancamento", class: "overline red--text" }
    ]
  }),
  mounted() {
    this.ActionLoadPageAlbuns();
  },
  computed: {
    ...mapState("music", ["albuns"])
  },
  methods: {
    ...mapActions("music", ["ActionLoadPageAlbuns"]),
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
#albuns {
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