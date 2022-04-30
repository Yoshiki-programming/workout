<template>
  <v-app>
    <v-app-bar color="success" dark app>
      <v-toolbar-title>WORKOUT APP</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn text to="/">HOME</v-btn>
        <v-btn text to="/editor">ADD WORKOUT</v-btn>
      </v-toolbar-items>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
    <v-footer color="success" dark app class="justify-center">
      presented by Yoshiki
    </v-footer>
  </v-app>
</template>
