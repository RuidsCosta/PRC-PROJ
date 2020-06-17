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
      { text: "Álbum", sortable: true, value: "album", class: "overline red--text" },
      { text: "Artista", sortable: true, value: "artista", class: "overline red--text" },
      { text: "Data Lançamento", sortable: true, value: "data_lancamento", class: "overline red--text" }
    ]
  }),
  mounted() {
    this.ActionLoadPageAlbuns();
  },
  computed: {
    ...mapState("music", ["albuns"])
  },
  methods: {
    ...mapActions("music", ["ActionLoadPageAlbuns"])
  }
};
</script>

<style scoped>
#albuns {
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