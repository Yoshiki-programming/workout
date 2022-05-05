<template>
  <div>
    <v-container>
      <h2 class="mb-5">{{ workout.workout }}</h2>
      <p>部位：{{ workout.part_of_body }}</p>
      <p>メモ：{{ workout.memo }}</p>
    </v-container>
    <v-btn :to="{ name: 'MyRecord', params: { id: this.id } }"
      >記録を見る</v-btn
    >
    <v-btn :to="{ name: 'MyEditor', params: { id: this.id } }">編集する</v-btn>
    <v-btn color="error" @click="deleteWorkoutData">削除する</v-btn>
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
