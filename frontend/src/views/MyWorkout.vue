<template>
  <div>
    <v-container>
      <h2 class="mb-5">{{ workout.workout }}</h2>
      <p>body part：{{ workout.part_of_body }}</p>
      <p>memo：{{ workout.memo }}</p>
    </v-container>
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
  },
  created() {
    this.getWorkoutData();
  },
};
</script>

<style></style>
