<template>
  <v-app id="home">
    <Navbar />
    <v-content>
      <v-container fluid style="padding: 0%">
        <v-img src="../assets/topo.png" height="210px">
          <div>
            <h1 style="margin: 60px 0px 0px 730px">Explora</h1>
            <h4 style="margin-left: 730px">Encontra aqui as tuas músicas, álbuns e artistas favoritos.</h4>
        </div>
        </v-img>
      </v-container>
      <v-container fluid>
        <v-row>
          <h3 style="padding-left: 12px">Artistas em destaque</h3>
          <v-spacer></v-spacer>
          <a @click="moreArtists()"><h3 style="padding-right: 12px">Ver mais ></h3></a>
        </v-row>
        <hr />
        <v-container fluid style="padding: 0%">
          <v-row>
            <v-col v-for="i in 7" :key="i" class="child-flex">
              <v-card class="d-inline-block" @click="goToArtist(`${ artistas[i + countArtists].id_artista }`)">
                <v-img height="190" width="190" :src="`${ artistas[i + countArtists].imagem }`"></v-img>
                <h4 class="mt-2">{{ artistas[i + countArtists].artista }}</h4>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-container>
      <v-container fluid>
        <v-row>
          <h3 style="padding-left: 12px">Álbuns recentes</h3>
          <v-spacer></v-spacer>
          <a @click="moreAlbums()"><h3 style="padding-right: 12px">Ver mais ></h3></a>
        </v-row>
        <hr />
        <v-container fluid style="padding: 0%">
          <v-row>
            <v-col v-for="i in 7" :key="i" class="child-flex">
              <v-card class="d-inline-block" @click="goToAlbum(`${ albuns[i + countAlbums].id_album }`)">
                <v-img height="190" width="190" :src="`${ albuns[i + countAlbums].capa }`"></v-img>
                <h4 class="mt-2">{{ albuns[i + countAlbums].album }}</h4>
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
  data: function() {
    return {
      countArtists: 0,
      countAlbums: 0,
    }
  },
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
    ...mapActions("music", ["ActionLoadPageHome"]),
    goToArtist(item) {
      this.$router.push(`/artistas/${item}`)
    },
    goToAlbum(item) {
      this.$router.push(`/albuns/${item}`)
    },
    moreArtists() {
      return this.countArtists = this.countArtists + 7
    },
    moreAlbums() {
      return this.countAlbums = this.countAlbums + 7
    }
  }
};
</script>

<style scoped>
#home {
  background-color: black;
}

.v-card {
  background-color: black;
  cursor: pointer;
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