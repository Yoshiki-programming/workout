<template>
  <div>
    <v-row justify="center" class="my-5">
      <div>記録の修正</div>
    </v-row>
    <v-card outlined class="mx-2">
      <v-container>
        <h2 class="text-center">
          <p v-if="record.workout">{{ record.workout.workout }}</p>
        </h2>
        <p>重さ：{{ record.weight }} KG</p>
        <p>回数：{{ record.reps }}</p>
        <p>メモ：{{ record.memo }}</p>
        <p>日付：{{ record.date }}</p>
      </v-container>
    </v-card>
    <v-row justify="center">
      <v-btn
        v-if="record.workout"
        :to="{ name: 'MyRecord', params: { id: record.workout.id } }"
        color="primary"
        text
        class="mx-2 my-5"
        >戻る</v-btn
      >
      <v-btn
        v-if="record"
        :to="{ name: 'RecordEdit', params: { id: this.id } }"
        color="primary"
        class="mx-2 my-5"
        text
        >編集</v-btn
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
        this.$router.push({
          name: "MyRecord",
          params: { id: this.record.workout.id },
        });
      });
    },
  },
  created() {
    this.getRecordData();
    console.log(this.record);
    // console.log(this.id);
  },
};
</script>

<style></style>
