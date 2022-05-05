<template>
  <div>
    <v-container>
      <p v-if="record.workout">{{ record.workout.workout }}</p>
      <p>重さ：{{ record.weight }} KG</p>
      <p>回数：{{ record.reps }}</p>
      <p>メモ：{{ record.memo }}</p>
      <p>日付：{{ record.date }}</p>
    </v-container>
    <v-btn
      v-if="record.workout"
      :to="{ name: 'MyRecord', params: { id: record.workout.id } }"
      >戻る</v-btn
    >
    <v-btn v-if="record" :to="{ name: 'RecordEdit', params: { id: this.id } }"
      >編集</v-btn
    >
    <v-btn color="error" @click="deleteRecordData">削除する</v-btn>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";

export default {
  name: "RecordEdit",
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
    setPageTitle(title) {
      document.title = title;
    },
    getRecordData() {
      let endpoint = `/api/workout-records/${this.id}/record`;
      apiService(endpoint).then((data) => {
        this.record = data;
      });
    },
    deleteRecordData() {
      let endpoint = `/api/workout-records/${this.id}/record`;
      apiService(endpoint, "DELETE").then(() => {
        this.$router.go({ path: this.$router.currentRoute.path, force: true });
      });
    },
  },
  created() {
    this.getRecordData();
    console.log(this.id);
  },
};
</script>

<style></style>
