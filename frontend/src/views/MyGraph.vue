<template>
  <div>
    <v-main>
      <v-card outlined class="mx-2">
        <div>{{ this.id }}</div>
        <chart></chart>
      </v-card>
      <v-row justify="center">
        <v-btn
          v-if="this.workoutrecords[0]"
          :to="{
            name: 'MyRecord',
            params: { id: this.id },
          }"
          color="primary"
          text
          class="mx-2 my-5"
          >戻る
        </v-btn>
      </v-row>
    </v-main>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";
export default {
  name: "MyGraph",
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      workoutrecords: [],
      workout_id: null,
      weight: null,
      reps: null,
      date: null,
      memo: null,
      next: null,
      loading: false,
      name: null,
    };
  },
  methods: {
    getWorkoutRecords() {
      let endpoint = `/api/workout-records/${this.id}/`;
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
        console.log(this.workoutrecords);
      });
    },
  },
  created() {
    this.getWorkoutRecords();
    // console.log("record", this.workoutrecords);
    // console.log("id:", this.id);
  },
};
</script>
