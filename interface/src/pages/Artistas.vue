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
                label="Search"
                single-line
                hide-details
              ></v-text-field>
            </v-card-title>
            <v-data-table :headers="headers" :items="artistas" :search="search"></v-data-table>
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
      { text: "Artista", sortable: true, value: "artista", class: "overline" },
      { text: "Gênero", sortable: false, value: "generos", class: "overline" },
      { text: "Popularidade", sortable: true, value: "popularidade", class: "overline" },
      { text: "Seguidores", sortable: true, value: "seguidores", class: "overline" }
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
hr {
    border: 1px solid red;
}
</style>