<template>
  <section>
    <v-container class="col-md-5">
    <h1>Escolha genres de Livros do seu Gosto</h1>
    <h3>{{texto}}</h3>
    <v-select
      :items = "items"
      item-value = "id"
      item-text = "name"
      label = "Estilos de Livros"
      attach
      multiple
      chips
      v-model = "escolha"
    >
    </v-select>
    <h3>Minha escolha</h3>
    <div class="col-md-15 " align="center"  >
    <v-container fluid grid-list-xl>
      <h1 class="Livros Sugeridos" align="center"></h1>
      <v-layout wrap justify-space-around>
      <v-flex v-for="(genre,i) in booksgenre" v-bind:key="i">
        <div  v-for="choice in escolha" v-bind:key="choice">

           <v-card height="200px" width="240px" 
       v-if="choice == genre.genre"
        >
       
          <p>{{genre.book}}</p>
        <p>{{genre.namebook}}</p>
        <p>{{genre.genre}}</p>
        <p>{{genre.namegenre}}</p>
        
        
        <!-- <p>{{book.description}}</p>
        <p>{{book.genre_name}}</p> -->
        <v-btn class="ma-2" text icon color="red lighten-2">
          <v-icon class="delete" @click="deleteBook(book)"></v-icon>
        </v-btn>
        <v-btn class="ma-2" text icon color="green">
          <v-icon class="edit" @click="editBook(book)"></v-icon>
        </v-btn>
        <v-divider></v-divider>
        </v-card>

        </div>
       
      </v-flex>
      </v-layout>
      
  </v-container>
  </div>
    </v-container>
  </section>
</template>

<script>
import axios from "axios";
import router from "@/router/"

export default {
    name: "Experiments",
    data () {
      return  {
        texto: "genres Literarios",
        genres: [],
        booksgenre: [],
        escolha: [],
      }
    },
    created() {
      this.getGenres(),
      this.getBGenres()
    },
    methods: {
      getGenres() {
        axios
        .request({
          baseURL: "http://127.0.0.1:8000",
          method: "get",
          url: "/api/genres/"
        })
        .then(response => {
          this.items = response.data
          console.log(response)
        });
      },
      getBGenres() {
        axios
        .request({
          baseURL: "http://127.0.0.1:8000",
          method: "get",
          url: "/api/booksgenre/"
        })
        .then(response => {
          this.booksgenre = response.data
          console.log(response)
        });
      }
    }
}
</script>

<style>

</style>