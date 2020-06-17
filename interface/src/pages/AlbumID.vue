<template>
  <v-app id="albumID">
    <Navbar />
    <v-content>
      <v-container fluid style="padding: 0%">
        <div id="topo"></div>
        <v-row id="img">
          <v-col cols="auto">
            <v-img height="250" width="250" :src="`${ albuns[0].capa }`"></v-img>
          </v-col>
          <v-col cols="auto" class="text-left pl-4">
            <v-row class="flex-column ma-0 fill-height" justify="center">
              <v-col class="px-0">
                <h1>{{ albuns[0].album }}</h1>
              </v-col>
              <v-col class="px-0">
                <h3>{{ albuns[0].artista }}</h3>
              </v-col>
              <v-col class="px-0 black--text">
                <h4>Data de lançamento {{ albuns[0].data_lancamento }}</h4>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-container>
      <v-container fluid style="padding: 0%">
        <v-simple-table id="table">
          <template v-slot:default>
            <thead>
              <tr>
                <th class="overline red--text">Faixas</th>
                <th class="overline red--text">Explícito</th>
                <th class="overline red--text">Duração</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="i in musicas" :key="i">
                <td>{{ i.musica }}</td>
                <td>{{ i.explicita }}</td>
                <td>{{ i.duracao }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import Navbar from "../components/Navbar";
import { mapActions, mapState } from "vuex";

export default {
  name: "albumID",
  components: {
    Navbar
  },
  mounted() {
    this.ActionLoadPageAlbumID(this.$route.params.id);
  },
  computed: {
    ...mapState("music", ["albuns", "musicas"])
  },
  methods: {
    ...mapActions("music", ["ActionLoadPageAlbumID"])
  }
};
</script>

<style scoped>
#topo {
  width: 100%;
  height: 200px;
  background-color: #D50000;
}

#img {
  margin-top: -160px;
  margin-left: 50px;
}

#table {
  font-family: Georgia, "Times New Roman", Times, serif;
  margin-left: 60px;
  margin-right: 60px;
}

h1 {
  font-size: 2.5em;
  color: white;
  font-family: Georgia, "Times New Roman", Times, serif;  
}

h3 {
  color: white;
  font-family: Georgia, "Times New Roman", Times, serif;
}

h4 {
  color: black;
  font-family: Georgia, "Times New Roman", Times, serif; 
}
</style>