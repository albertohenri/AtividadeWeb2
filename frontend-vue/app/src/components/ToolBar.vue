<template>
  <v-app-bar app :clipped-left="$vuetify.breakpoint.lgAndUp" color="indigo" dark>
    <v-app-bar-nav-icon 
      @click.stop="$emit('toggle-drawer')"
    > </v-app-bar-nav-icon>    
    <v-toolbar-title>Books & Books</v-toolbar-title>
  </v-app-bar>
</template>

<script>
import eventBus from "../main"
export default {
  name: 'ToolBar',
  props: ['drawer'],
  methods: {
    updateAppDrawer() {
      eventBus.$emit('updateAppDrawer')
    }
  }
}
</script>