<template>
  <div>
    <v-container>
      <h1>Workout List</h1>
      <div v-for="workout in workouts" :key="workout.pk">
        <h2>
          <router-link
            :to="{ name: 'workout', params: { id: workout.id } }"
            class="workout-link"
            >{{ workout.workout }} {{ workout.part_of_body }}
          </router-link>
        </h2>
      </div>
    </v-container>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";
export default {
  name: "MyHome",
  data() {
    return {
      workouts: [],
    };
  },
  methods: {
    getWorkouts() {
      let endpoint = "api/workouts/";
      apiService(endpoint).then((data) => {
        this.workouts.push(...data.results);
      });
    },
  },
  created() {
    this.getWorkouts();
    console.log(this.workouts);
  },
};
</script>
