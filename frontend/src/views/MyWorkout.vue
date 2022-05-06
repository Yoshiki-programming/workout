<template>
  <div>
    <v-row justify="center" class="my-5">
      <v-btn color="primary" :to="{ name: 'MyRecord', params: { id: this.id } }"
        >記録</v-btn
      >
    </v-row>
    <v-row justify="center" class="my-5">
      <div>{{ workout.workout }}の記録を確認する</div>
    </v-row>
    <v-card outlined class="mx-2">
      <v-container>
        <p class="mb-5">{{ workout.workout }}</p>
        <p>部位：{{ workout.part_of_body }}</p>
        <p>メモ：{{ workout.memo }}</p>
      </v-container>
    </v-card>
    <v-row justify="center">
      <v-btn color="primary" :to="{ name: 'home' }" text class="mx-2 my-5"
        >戻る</v-btn
      >
      <v-btn
        color="primary"
        :to="{ name: 'MyEditor', params: { id: this.id } }"
        text
        class="mx-2 my-5"
        >編集</v-btn
      >
      <v-btn color="error" @click="deleteWorkoutData" class="my-5">削除</v-btn>
    </v-row>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";

export default {
  name: "MyWorkout",
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      workout: {},
      body_items: ["腹", "腕", "背中", "胸", "脚", "肩"],
    };
  },
  methods: {
    setPageTitle(title) {
      document.title = title;
    },
    getWorkoutData() {
      let endpoint = `/api/workouts/${this.id}/`;
      apiService(endpoint).then((data) => {
        this.workout = data;
        this.setPageTitle(data.workout);
      });
    },
    deleteWorkoutData() {
      let endpoint = `/api/workouts/${this.id}/`;
      apiService(endpoint, "DELETE").then(() => {
        this.$router.push({
          name: "home",
        });
      });
    },
  },
  created() {
    this.getWorkoutData();
    // console.log(location.href);
  },
};
</script>

<style></style>
