<template>
  <section>
    <v-container class="col-md-5">
    <h1>Escolha Generos de Livros do seu Gosto</h1>
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
    {{escolha}}
    </v-container>
  </section>
</template>

<script>
import axios from "axios"
export default {
    name: "Experiments",
    data () {
      return  {
        texto: "Generos Literarios",
        items: [],
        escolha: "",
      }
    },
    created() {
      this.getGenres()
    },
    methods: {
      getGenres() {
        axios
        .request({
          baseURL: "http://localhost:8000",
          method: "get",
          url: "/api/genres/"
        })
        .then(response => {
          this.items = response.data
          console.log(response)
        });
      }
    }
}
</script>

<style>

</style>