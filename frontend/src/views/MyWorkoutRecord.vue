<template>
  <div>
    <v-container style="size: 150px">WORKOUT RECORD</v-container>
    <v-main>
      <div v-for="record in workoutrecords" :key="record.pk">
        <h2>
          <router-link
            :to="{ name: 'workoutrecord', params: { id: record.id } }"
            class="workoutrecord-link"
          >
            <v-card>
              <v-card-title> {{ record.workout.workout }}</v-card-title>
              <v-card-text style="size: 50px"
                >{{ record.weight }} KG</v-card-text
              >
              <v-card-text style="size: 50px"
                >{{ record.reps }} REPS</v-card-text
              >
              <v-card-text style="size: 50px"
                >MEMO：{{ record.memo }}</v-card-text
              >
              <v-card-text style="size: 50px">{{ record.date }}</v-card-text>
            </v-card>
          </router-link>
        </h2>
      </div>
      <div class="my-4">
        <p v-show="loading">...loading...</p>
        <v-btn v-show="next" @click="getWorkoutRecords" color="success"
          >Load More
        </v-btn>
      </div>
    </v-main>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";
export default {
  name: "MyWorkoutRecord",
  data() {
    return {
      workoutrecords: [],
      workout: null,
      weight: null,
      reps: null,
      date: null,
      memo: null,
      next: null,
      loading: false,
    };
  },
  methods: {
    getWorkoutRecords() {
      let endpoint = "api/workout-records/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loading = true;
      apiService(endpoint).then((data) => {
        this.workoutrecords.push(...data.results);
        this.loading = false;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    },
  },
  created() {
    this.getWorkoutRecords();
    console.log(this.workoutrecords);
  },
};
</script>
