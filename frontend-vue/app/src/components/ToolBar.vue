
<style>
.textcolor{
  color: white;
}
</style>

<template>
  <div>
    <v-toolbar
      max-height="70"
      max-width="1920"
      color="red lighten-1"
    >
        <v-spacer></v-spacer>

      <v-divider vertical></v-divider>  
      <v-toolbar-items v-for="item in items" :key="item.title">
        
        <v-btn max-height="70" text :to="item.endpoint"><v-icon max-height="70" icon>{{ item.icon }}</v-icon>{{item.title}}</v-btn>
        <v-divider vertical></v-divider>
        
      </v-toolbar-items>
      <v-spacer></v-spacer>
      

    </v-toolbar>
  </div>
  
</template>



<script>
export default {
  name: "toolbar",
  data() {
    return {
      authenticated: false,
      user: {},
      items: [
        { title: "Home", icon: "mdi-home-city", endpoint: '/' },
        { title: "My Account", icon: "mdi-account", endpoint: '/user' },
        { title: "Users", icon: "mdi-account-group", endpoint: '/users' },
        { title: "Books", icon: "mdi-library-books", endpoint: '/books'},
        { title: "Experiments", icon: "mdi-chart-pie", endpoint: '/experiments'},
        { title: "Logout", icon: "mdi-logout", endpoint: '/logout'}
      ],
      icons: [
        { icon: "mdi-delete-circle"}
      ]
    };
  },
  mounted() {
    this.checkAuthenticated();
  },
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