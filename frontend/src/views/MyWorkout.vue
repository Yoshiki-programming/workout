<template>
  <div>
    <v-container>
      <h2 class="mb-5">{{ workout.workout }}</h2>
      <p>BODY PART：{{ workout.part_of_body }}</p>
      <p>MEMO：{{ workout.memo }}</p>
    </v-container>
    <v-btn to="/workout-records">RECORD</v-btn>
    <v-btn :to="{ name: 'editor', params: { id: workout.id } }"
      >EDIT WORKOUT</v-btn
    >
    <v-btn to="/">DELETE WORKOUT</v-btn>
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
    console.log(this.workout);
  },
};
</script>

<style></style>
