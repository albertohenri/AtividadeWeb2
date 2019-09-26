<template>
  <v-app id="inspire">
    <v-content>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="4">
            <v-card class="elevation-20">
              <v-alert
                v-model="errorShow"
                :dismissible=true
                type="error"
                class="mb-4"
              >
                Login or password wrong
              </v-alert>
              <v-toolbar color="primary" dark flat>
                <v-toolbar-title>Authentication</v-toolbar-title>
                <div class="flex-grow-1"></div>                
              </v-toolbar>
              <v-card-text>
                <v-form ref="form">
                  <v-text-field 
                    label="Login"
                    v-model="credentials.username"
                    name="login" 
                    prepend-icon="person" 
                    type="text"
                    :rules="rules.username"
                    required
                  ></v-text-field>

                  <v-text-field
                    id="password"
                    v-model="credentials.password"
                    label="Password"
                    name="password"
                    prepend-icon="lock"
                    type="password"
										:rules="rules.password"
                    required
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <div class="flex-grow-1"></div>
                <v-btn color="primary" @click="login">Login</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import router from "../router";
import axios from "axios";

 
export default {  
  name: "Login",
  props: {
    source: String,
  }, 
  data: () => ({
    credentials: {},
    errorShow: false,
    drawer: null,
    rules: {
      username: [v => !!v || "Usuário é obrigatório."],
      password: [
        v => !!v || "Senha é obrigatória.",
        v => (v && v.length > 5) || "A senha deve ser maior que 5 caracteres."
      ]
    }
  }),
  methods: {
    login() {
      if (this.$refs.form.validate()) {
        axios
          .post("http://localhost:8000/auth/token/login", this.credentials)
          .then(res => {
            this.$session.start();
            this.$session.set("token", res.data.auth_token);
            router.push("/");
          })
          .catch(e => {
            this.errorShow = true
            console.log(e)
          });
      }
    }
  }
};
</script>