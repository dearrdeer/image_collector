
<template>
  <v-app>
    <v-app-bar
      app
      color="green"
    >
      <v-app-bar-nav-icon @click="drawer = !drawer" />
      <span class="title ml-3 mr-5">Virtual&nbsp;
        <span class="font-weight-light">Assistant
        </span>
      </span>
      <v-text-field
        solo-inverted
        flat
        hide-details
        label="Search"
      />
      <v-toolbar-items>
        <v-btn text small href="../">Home</v-btn>
        <newPres></newPres>
      </v-toolbar-items>
    </v-app-bar>
    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
import Create from '@/views/Create.vue';
// import axios from 'axios';

export default {
  name: 'App',
  components: {
    newPres: Create,
  },
};
</script>
