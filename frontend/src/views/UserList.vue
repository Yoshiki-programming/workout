<template>
  <div>
    <v-row justify="center" class="my-5">
      <div>ユーザー情報</div>
    </v-row>
    <v-card outlined class="mx-2">
      <v-container>
        <h2 class="text-center">
          <p>{{ record.username }} さん</p>
        </h2>
        <p>身長：{{ record.heights }} cm</p>
        <p>体重：{{ record.weights }} kg</p>
      </v-container>
    </v-card>
    <v-row justify="center">
      <v-btn :to="{ name: 'home' }" color="primary" text class="mx-2 my-5"
        >ホームへ</v-btn
      >
      <v-btn color="error" @click="deleteRecordData" class="mx-2 my-5"
        >削除する</v-btn
      >
    </v-row>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";

export default {
  name: "UserList",
  data() {
    return {
      record: {
        type: Object,
      },
    };
  },
  methods: {
    setPageTitle() {
      document.title = "ユーザー情報";
    },
    getRecordData() {
      let endpoint = `/api/user/`;
      apiService(endpoint).then((data) => {
        this.record = data.results[0];
      });
    },
    deleteRecordData() {
      let endpoint = `/api/user/${this.id}/`;
      apiService(endpoint, "DELETE").then(() => {
        this.$router.push({
          name: "home",
        });
      });
    },
  },
  mounted() {
    this.getRecordData();
    this.setPageTitle();
    console.log(this.record);
    // console.log(this.id);
  },
};
</script>

<style></style>
