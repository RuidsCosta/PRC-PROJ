<template>
  <v-app id="artistaID">
    <Navbar />
    <v-content>
      <v-container fluid style="padding: 0%">
        <v-row id="img">
          <v-col cols="auto">
            <v-img height="250" width="250" :src="`${ artistas[0].imagem }`"></v-img>
          </v-col>
          <v-col cols="auto" class="text-left pl-4">
            <v-row class="flex-column ma-0 fill-height" justify="center">
              <v-col class="px-0">
                <h1>{{ artistas[0].artista }}</h1>
              </v-col>
              <v-col class="px-0">
                <h3>Gêneros: {{ artistas[0].generos }}</h3>
              </v-col>
              <v-col class="px-0">
                <h3>Popularidade: {{ artistas[0].popularidade }}</h3>
              </v-col>
              <v-col class="px-0">
                <h3>Seguidores: {{ artistas[0].seguidores }}</h3>
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
            <v-col v-for="i in albuns" :key="i.id_album" class="child-flex" cols="auto">
              <v-card class="d-inline-block" max-width="190" >
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
    ...mapState("music", ["albuns", "artistas"])
  },
  methods: {
    ...mapActions("music", ["ActionLoadPageArtistaID"])
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