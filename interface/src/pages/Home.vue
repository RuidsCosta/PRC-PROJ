<template>
  <v-app id="home">
    <Navbar />
    <v-content>
      <v-container fluid style="padding: 0%">
        <v-img src="../assets/topo.png" height="210px">
          <div>
            <h1 style="margin: 60px 0px 0px 730px">Explore</h1>
            <h4 style="margin-left: 730px">Aqui tu encontras o melhor acervo musical para a tua playlist.</h4>
        </div>
        </v-img>
      </v-container>
      <v-container fluid>
        <h3>Artistas em destaque</h3>
        <hr />
        <v-container fluid style="padding: 0%">
          <v-row>
            <v-col v-for="i in 7" :key="i" class="child-flex">
              <v-card class="d-inline-block">
                <v-img height="190" width="190" :src="`${ artistas[i].imagem }`"></v-img>
                <h4 class="mt-2">{{ artistas[i].artista }}</h4>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-container>
      <v-container fluid>
        <h3>Álbuns em destaque</h3>
        <hr />
        <v-container fluid style="padding: 0%">
          <v-row>
            <v-col v-for="i in 7" :key="i" class="child-flex">
              <v-card class="d-inline-block">
                <v-img height="190" width="190" :src="`${ albuns[i].capa }`"></v-img>
                <h4 class="mt-2">{{ albuns[i].album }}</h4>
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
  name: "home",
  components: {
    Navbar
  },
  mounted() {
    this.ActionLoadPageHome();
  },
  computed: {
    ...mapState("music", ["artistas", "albuns", "musicas"])
  },
  methods: {
    ...mapActions("music", ["ActionLoadPageHome"])
  }
};
</script>

<style scoped>
#home {
  background-color: black;
}

.v-card {
  background-color: black;
}

h1,
h3,
h4 {
  color: white;
  font-family: Georgia, 'Times New Roman', Times, serif;
}

hr {
    border: 1px solid red;
}
</style>