<style >


</style>


<template>
  <div class="col-md-15 " align="center"  >
    <v-container fluid grid-list-xl>
      <h1 class="Livros Sugeridos" align="center"></h1>
      <v-layout wrap justify-space-around>
      <v-flex v-for="book in books" v-bind:key="book.id">
        <v-card height="200px" width="240px">
        <p>{{book.name}}</p>
        <p>{{book.author}}</p>
        <p>{{book.description}}</p>
        <p>{{book.genre_name}}</p>
        <v-btn class="ma-2" text icon color="red lighten-2">
          <v-icon class="delete" @click="deleteBook(book)"></v-icon>
        </v-btn>
        <v-btn class="ma-2" text icon color="green">
          <v-icon class="edit" @click="editBook(book)"></v-icon>
        </v-btn>
        <v-divider></v-divider>
        </v-card>
      </v-flex>
      <CreateBooks @updateBooks="all"></CreateBooks>
      </v-layout>
      
  </v-container>
  </div>
</template>


<script>
import axios from "axios";
import router from "@/router/"
import CreateBooks from "./Create";

export default {
  name: "ListBooks",
  data() {
    return {
      books: [],
    };
  },
  components: {
    CreateBooks: CreateBooks,
  },
  created() {
    this.all();
  },
  methods: {
    all() {
      axios
        .request({
          baseURL: "http://127.0.0.1:8000",
          method: "get",
          url: "/api/books/"
        })
        .then(response => {
          this.books = response.data
          console.log(response)
        });
    },
    deleteBook(book) {
      if (confirm("Excluir " + book.name)) {
        axios
          .delete(`http://127.0.0.1:8000/api/books/${book.id}`, {
            headers: {
              Authorization: `Token ${this.$session.get("token")}`
            }
          })
          .then(response => {
            this.all()
            console.log(response)
          });
      }
    },
    editBook(book) {
      router.push(`/books/edit/${book.id}`)
    }
  }
};
</script>