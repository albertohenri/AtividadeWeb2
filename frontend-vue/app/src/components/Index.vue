<template>
  <section class="container">
    <h1>Página principal</h1>
    
    <button v-if="authenticated">Logout</button>
    <div id="app">
  <v-app id="inspire">
    <v-card
      class="mx-auto"
      max-width="344"
    >
      <v-img
        img src="../assets/livro1.png" class="d-block w-100" alt="Menino Maluquinho"
        height="200px"
      ></v-img>
  
      <v-card-title>
        Top western road trips
      </v-card-title>
  
      <v-card-subtitle>
        1,000 miles of wonder
      </v-card-subtitle>
  
      <v-card-actions>
        <v-cart-text text>Informaçoes</v-cart-text>

  
        <v-spacer></v-spacer>
  
        <v-btn
          icon
          @click="show = !show"
        >
          <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
        </v-btn>
      </v-card-actions>
  
      <v-expand-transition>
        <div v-show="show">
          <v-divider></v-divider>
  
          <v-card-text>
            O Menino Maluquinho é uma série de histórias em quadrinhos brasileira criada pelo desenhista e cartunista Ziraldo. A revista foi baseada no livro infantil de mesmo nome publicado em 1980, que se tornou um fenômeno durante os anos de 1990 e 2000.
          </v-card-text>
        </div>
      </v-expand-transition>
    </v-card>
  </v-app>
</div>
  </section>
  
</template>

<script>
import router from "../router";

export default {
  name: "Index",
  name:"#app",
  data() {
    return {
      authenticated: false,
      show: false
    };
  },
  mounted() {
    this.checkAuthenticated();
  },
  name: "#app",
  

  methods: {
    checkAuthenticated() {
      this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/login");
      } else {
        this.authenticated = true;
      }
    }
  }
};
</script>
