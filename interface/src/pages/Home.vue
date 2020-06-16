<template>
  <v-app id="home">
    <Navbar />
    <v-content>
      <v-container fluid style="padding: 0%">
        <v-img src="../assets/topo.png" height="210px"></v-img>
      </v-container>
      <v-container fluid>
        <h3>Artistas em destaque</h3>
        <hr />
        <v-container fluid style="padding: 0%">
          <v-row>
            <v-col v-for="n in 7" :key="n" class="child-flex">
              <v-card>
                <v-img
                  :src="`https://picsum.photos/500/300?image=${n * 5 + 10}`"
                  aspect-ratio="1"
                  class="grey lighten-2"
                ></v-img>
                <h4 class="mt-2">Artista</h4>
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
            <v-col v-for="n in 7" :key="n" class="child-flex">
              <v-card>
                <v-img
                  :src="`https://picsum.photos/500/300?image=${n * 15 + 20}`"
                  aspect-ratio="1"
                  class="grey lighten-2"
                ></v-img>
                <h4 class="mt-2">Álbum</h4>
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

h3,
h4 {
  color: white;
}

hr {
    border: 1px solid red;
}
</style>