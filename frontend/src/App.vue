<template>
  <v-app>
    <v-app-bar color="success" dark app>
      <v-toolbar-title><v-btn text to="/">WORKOUT APP</v-btn></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn text to="/">HOME</v-btn>
      </v-toolbar-items>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
    <v-footer color="success" dark app class="justify-center">
      developed by Yoshiki
    </v-footer>
  </v-app>
</template>
