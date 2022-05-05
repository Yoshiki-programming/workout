<template>
  <v-app>
    <v-app-bar color="success" dark app>
      <v-toolbar-title><v-btn text to="/">筋トレの記録</v-btn></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn text to="/">ホームへ</v-btn>
      </v-toolbar-items>
    </v-app-bar>
    <v-main>
      <v-container></v-container>
      <router-view />
    </v-main>
    <v-footer color="success" dark app class="justify-center">
      developed by Yoshiki
    </v-footer>
  </v-app>
</template>
<script>
import { apiService } from "../src/common/api.service.js";
export default {
  name: "App",
  data() {
    return {
      workouts: [],
      user: null,
    };
  },
  methods: {
    getWorkouts() {
      let endpoint = "api/workouts/";
      apiService(endpoint).then((data) => {
        this.workouts.push(...data.results);
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    },
  },
  created() {
    this.getWorkouts();
    console.log(this.workouts);
  },
};
</script>
