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
      { text: "Artista", sortable: true, value: "artista", class: "overline red--text" },
      { text: "Gênero", sortable: false, value: "generos", class: "overline red--text" },
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
    ...mapActions("music", ["ActionLoadPageArtistas"])
  }
};
</script>

<style scoped>
#artistas {
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