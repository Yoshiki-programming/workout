<template>
  <v-app>
    <v-app-bar color="#1D1DF" dark app>
      <v-toolbar-title><v-btn to="/">ホーム</v-btn></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn text :to="{ name: 'UserList' }">ユーザー情報</v-btn>
        <v-btn text href="/auth/logout/">ログアウト</v-btn>
      </v-toolbar-items>
    </v-app-bar>
    <v-main>
      <v-container></v-container>
      <router-view />
    </v-main>
    <v-footer dark app color="#1D1DF" class="justify-center">
      developed by Yoshiki
    </v-footer>
  </v-app>
</template>
