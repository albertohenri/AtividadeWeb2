<style>
</style>



<template>
  <section class="container">
    <!-- <h1>Página principal</h1>
    
    <button v-if="authenticated">Logout</button>-->
    <v-card-title primary-title center>
        <h2>Livraria IFC</h2>
    </v-card-title>
    
    <br />
    <br />
    <br />


        <v-carousel>
          <v-carousel-item
            v-for="(item,i) in items"
            :key="i"
            :src="item.src"
            reverse-transition="fade-transition"
            transition="fade-transition"
          ></v-carousel-item>
        </v-carousel>

    <!-- Card 1 -->
    <v-container fluid grid-list-xl>
      <h1 class="Titulo" align="center">Resenhas Literarias</h1>
      <v-layout wrap justify-space-around>
        <v-flex>
          <v-row align="center" justify="center">
            <v-container fluid>
              <v-row justify="space-around">
                <v-col cols="4">
                  <v-hover v-slot:default="{ hover }">
                    <v-card
                      :elevation="hover ? 12 : 2"
                      class="mx-auto"
                      min-width="380"
                      max-width="380"
                      outlined
                    >
                      <v-list-item three-line>
                        <v-list-item-content>
                          <v-list-item-title class="headline mb-1">Menino maluquinho</v-list-item-title>
                          <v-list-item-subtitle>Ziraldo</v-list-item-subtitle>
                          <br />
                          <p>O Menino Maluquinho é uma série de histórias em quadrinhos brasileira criada pelo desenhista e cartunista Ziraldo. 
                              A revista foi baseada no livro infantil de mesmo nome publicado em 1980, </p>
                          <br />
                          <br />
                        </v-list-item-content>
                      </v-list-item>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn class="ma-2" text icon color="red lighten-2">
                          <v-icon class="delete" @click="deleteTeam(team)"></v-icon>
                        </v-btn>

                        <v-btn class="ma-2" text icon color="green">
                          <v-icon class="edit" @click="editTeam(team)"></v-icon>
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-hover>
                </v-col>
                <v-col cols="4">
                  <v-hover v-slot:default="{ hover }">
                    <v-card
                      :elevation="hover ? 12 : 2"
                      class="mx-auto"
                      min-width="380"
                      max-width="380"
                      outlined
                    >
                      <v-list-item three-line>
                        <v-list-item-content>
                          <v-list-item-title class="headline mb-1">Harry Potter</v-list-item-title>
                          <v-list-item-subtitle>Suspense</v-list-item-subtitle>
                          <br />
                          <p>A série narra as aventuras de um jovem chamado Harry James Potter, que descobre aos 11
                               anos de idade que é um bruxo ao ser convidado para estudar na Escola de Magia e Bruxaria de Hogwarts</p>
                          <br />
                          <br />
                        </v-list-item-content>
                      </v-list-item>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn class="ma-2" text icon color="red lighten-2">
                          <v-icon class="delete" @click="deleteTeam(team)"></v-icon>
                        </v-btn>

                        <v-btn class="ma-2" text icon color="green">
                          <v-icon class="edit" @click="editTeam(team)"></v-icon>
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-hover>
                </v-col>
                <v-col cols="4">
                  <v-hover v-slot:default="{ hover }">
                    <v-card
                      :elevation="hover ? 12 : 2"
                      class="mx-auto"
                      min-width="380"
                      max-width="380"
                      outlined
                    >
                      <v-list-item three-line>
                        <v-list-item-content>
                          <v-list-item-title class="headline mb-1">Em Busca das Estrelas</v-list-item-title>
                          <v-list-item-subtitle>Drama</v-list-item-subtitle>
                          <br />
                          <p>Asuna embarca em uma viagem até a terra dos mortos, Agartha, para encontrar seu pai e um jovem misterioso que salvou sua vida. 
                              A jornada promete ser difícil, já que entre o mundo dos vivos e dos mortos, 
                              há regras que devem ser respeitadas.</p>
                          <br />
                          <br />
                        </v-list-item-content>
                      </v-list-item>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn class="ma-2" text icon color="red lighten-2">
                          <v-icon class="delete" @click="deleteTeam(team)"></v-icon>
                        </v-btn>

                        <v-btn class="ma-2" text icon color="green">
                          <v-icon class="edit" @click="editTeam(team)"></v-icon>
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-hover>
                </v-col>
              </v-row>
            </v-container>
          </v-row>



          <v-row align="center" justify="center">
            <v-container fluid>
              <v-row justify="space-around">
                <v-col cols="4">
                  <v-hover v-slot:default="{ hover }">
                    <v-card
                      :elevation="hover ? 12 : 2"
                      class="mx-auto"
                      min-width="380"
                      max-width="380"
                      outlined
                    >
                      <v-list-item three-line>
                        <v-list-item-content>
                          <v-list-item-title class="headline mb-1">Homem-Aranha</v-list-item-title>
                          <v-list-item-subtitle>aventuras</v-list-item-subtitle>
                          <br />
                          <p>O Homem-Aranha alter-ego de Peter Parker, é um personagem fictício, um super-herói que aparece nas
                               revistas em quadrinhos americanas publicadas pela Marvel Comics,
                               existindo no seu universo partilhado.</p>
                          <br />
                          <br />
                        </v-list-item-content>
                      </v-list-item>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn class="ma-2" text icon color="red lighten-2">
                          <v-icon class="delete" @click="deleteTeam(team)"></v-icon>
                        </v-btn>

                        <v-btn class="ma-2" text icon color="green">
                          <v-icon class="edit" @click="editTeam(team)"></v-icon>
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-hover>
                </v-col>
                <v-col cols="4">
                  <v-hover v-slot:default="{ hover }">
                    <v-card
                      :elevation="hover ? 12 : 2"
                      class="mx-auto"
                      min-width="380"
                      max-width="380"
                      outlined
                    >
                      <v-list-item three-line>
                        <v-list-item-content>
                          <v-list-item-title class="headline mb-1">Vidas Secas</v-list-item-title>
                          <v-list-item-subtitle>Romance</v-list-item-subtitle>
                          <br />
                          <p>Vidas secas é o título do romance do escritor brasileiro Graciliano Ramos,
                               publicado em 1938, considerado por muitos como a maior obra do autor</p>
                          <br />
                          <br />
                        </v-list-item-content>
                      </v-list-item>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn class="ma-2" text icon color="red lighten-2">
                          <v-icon class="delete" @click="deleteTeam(team)"></v-icon>
                        </v-btn>

                        <v-btn class="ma-2" text icon color="green">
                          <v-icon class="edit" @click="editTeam(team)"></v-icon>
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-hover>
                </v-col>
                <v-col cols="4">
                  <v-hover v-slot:default="{ hover }">
                    <v-card
                      :elevation="hover ? 12 : 2"
                      class="mx-auto"
                      min-width="380"
                      max-width="380"
                      outlined
                    >
                      <v-list-item three-line>
                        <v-list-item-content>
                          <v-list-item-title class="headline mb-1">O Cortiço</v-list-item-title>
                          <v-list-item-subtitle>Romance</v-list-item-subtitle>
                          <br />
                          <p>DescriçãoO Cortiço é um romance naturalista do brasileiro Aluísio Azevedo publicado 
                              em 1890 que denuncia a exploração e as péssimas condições de vida dos moradores 
                              das estalagens ou dos cortiços cariocas do final do século XIX.</p>
                          <br />
                          <br />
                        </v-list-item-content>
                      </v-list-item>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn class="ma-2" text icon color="red lighten-2">
                          <v-icon class="delete" @click="deleteTeam(team)"></v-icon>
                        </v-btn>

                        <v-btn class="ma-2" text icon color="green">
                          <v-icon class="edit" @click="editTeam(team)"></v-icon>
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-hover>
                </v-col>
              </v-row>
            </v-container>
          </v-row>


          <v-row align="center" justify="center">
            <v-container fluid>
              <v-row justify="space-around">
                <v-col cols="4">
                  <v-hover v-slot:default="{ hover }">
                    <v-card
                      :elevation="hover ? 12 : 2"
                      class="mx-auto"
                      min-width="380"
                      max-width="380"
                      outlined
                    >
                      <v-list-item three-line>
                        <v-list-item-content>
                          <v-list-item-title class="headline mb-1">Dom Casmurro</v-list-item-title>
                          <v-list-item-subtitle>Romance</v-list-item-subtitle>
                          <br />
                          <p>Dom Casmurro é um romance escrito por Machado de Assis, publicado em 1899 pela Livraria Garnier.
                               Escrito para publicação em livro, o que ocorreu em 1900</p>
                          <br />
                          <br />
                        </v-list-item-content>
                      </v-list-item>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn class="ma-2" text icon color="red lighten-2">
                          <v-icon class="delete" @click="deleteTeam(team)"></v-icon>
                        </v-btn>

                        <v-btn class="ma-2" text icon color="green">
                          <v-icon class="edit" @click="editTeam(team)"></v-icon>
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-hover>
                </v-col>
                <v-col cols="4">
                  <v-hover v-slot:default="{ hover }">
                    <v-card
                      :elevation="hover ? 12 : 2"
                      class="mx-auto"
                      min-width="380"
                      max-width="380"
                      outlined
                    >
                      <v-list-item three-line>
                        <v-list-item-content>
                          <v-list-item-title class="headline mb-1">Grande Sertão: Veredas</v-list-item-title>
                          <v-list-item-subtitle>Ficçao</v-list-item-subtitle>
                          <br />
                          <p>Grande Sertão: Veredas é um romance experimental modernista escrito pelo autor brasileiro João Guimarães Rosa e publicado pela Livraria José Olympio Editora, em 1956.
                               Tanto a arte da capa como as ilustrações de Grande sertão: veredas são de autoria de Poty Lazzarotto.</p>
                          <br />
                          <br />
                        </v-list-item-content>
                      </v-list-item>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn class="ma-2" text icon color="red lighten-2">
                          <v-icon class="delete" @click="deleteTeam(team)"></v-icon>
                        </v-btn>

                        <v-btn class="ma-2" text icon color="green">
                          <v-icon class="edit" @click="editTeam(team)"></v-icon>
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-hover>
                </v-col>
                <v-col cols="4">
                  <v-hover v-slot:default="{ hover }">
                    <v-card
                      :elevation="hover ? 12 : 2"
                      class="mx-auto"
                      min-width="380"
                      max-width="380"
                      outlined
                    >
                      <v-list-item three-line>
                        <v-list-item-content>
                          <v-list-item-title class="headline mb-1">Capitães da Areia</v-list-item-title>
                          <v-list-item-subtitle>Ficção</v-list-item-subtitle>
                          <br />
                          <p>Capitães da Areia é um romance de autoria do escritor brasileiro Jorge Amado, escrito em 1937. 
                              A obra retrata a vida de um grupo de menores abandonados, que crescem nas ruas da cidade de Salvador, 
                              Bahia, vivendo em um trapiche, roubando para sobreviver, chamados de "Capitães da Areia"</p>
                          <br />
                          <br />
                        </v-list-item-content>
                      </v-list-item>
                    </v-card>
                  </v-hover>
                </v-col>
              </v-row>
            </v-container>
          </v-row>
          <br />
        </v-flex>
      </v-layout>
    </v-container>
    
  </section>
</template>

<script>
import router from "../router";
import axios from "axios";

export default {
  name: "Index",
  name: "#app",
  name: "cont",
  data() {
    return {
      authenticated: false,
      show: false,
      items: [
        {
          src:
            "https://beduka.com/blog/wp-content/uploads/2018/07/livros-fuvest-2019.jpg"
        },
        {
          src: "https://miro.medium.com/max/1600/1*722H7nWsDQ0D-ReOKoRytQ.jpeg"
        },
        {
          src:
            "https://nova-escola-producao.s3.amazonaws.com/DcbyH8T3DZmVmqkxpx9CE7BTV5MPxCryEeS5KzemPhzhRuuZDJGtN3TNhtsf/livros-editoracao.jpeg"
        },
        {
          src:
            "https://www.ofertasnodia.com/wp-content/uploads/2012/03/comprar-livros-promocao.jpg"
        }
      ]
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
    },
     deleteBook(book) {
      if (confirm("Excluir " + book.name)) {
        axios
          .delete(`http://localhost:8000/api/books/${book.id}`, {
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
