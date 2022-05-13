<template>
  <div>
    <v-row justify="center" class="my-5">
      <div>ユーザー情報</div>
    </v-row>
    <v-card outlined class="mx-2">
      <v-container>
        <p v-if="record.username">{{ record.username }} さん</p>
        <p>身長：{{ record.height }}</p>
        <p>体重：{{ record.weight }}</p>
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
  name: "UserInfo",
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      record: {},
    };
  },
  methods: {
    setPageTitle() {
      document.title = "ユーザー情報";
    },
    getRecordData() {
      let endpoint = `/api/user/${this.id}/`;
      apiService(endpoint).then((data) => {
        this.record = data;
        // console.log(this.record);
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
  created() {
    this.getRecordData();
    this.setPageTitle();
  },
};
</script>

<style></style>
