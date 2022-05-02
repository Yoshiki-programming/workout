<template>
  <div>
    <v-container style="size: 150px">SELECT OR ADD WORKOUT</v-container>
    <v-main>
      <v-row justify="center" style="">
        <v-dialog v-model="dialog" scrollable max-width="300px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="success" dark v-bind="attrs" v-on="on">
              + WORKOUT
            </v-btn>
          </template>
          <v-card style="">
            <v-card-title>ADD WORKOUT</v-card-title>
            <v-divider></v-divider>
            <v-card-text style="height: 300px">
              <form @submit.prevent="onSubmit">
                <v-select
                  v-model="part_of_body"
                  label="BODY PART"
                  :items="body_items"
                >
                </v-select>

                <v-text-field
                  v-model="workout"
                  label="MENU"
                  required
                ></v-text-field>

                <v-textarea v-model="memo" label="MEMO"></v-textarea>
                <v-btn color="success" text @click="dialog = false">
                  Close
                </v-btn>
                <v-btn color="success" type="submit" @click="dialog = false">
                  Save
                </v-btn>
              </form>
            </v-card-text>
            <v-divider></v-divider>
            <v-card-actions> </v-card-actions>
          </v-card>
        </v-dialog>
      </v-row>
      <div v-for="workout in workouts" :key="workout.pk">
        <h2>
          <router-link
            :to="{ name: 'workout', params: { id: workout.id } }"
            class="workout-link"
          >
            <v-card>
              <v-card-title> {{ workout.part_of_body }}</v-card-title>
              <v-card-text style="size: 50px">{{
                workout.workout
              }}</v-card-text>
            </v-card>
          </router-link>
        </h2>
      </div>
      <div class="my-4">
        <p v-show="loading">...loading...</p>
        <v-btn v-show="next" @click="getWorkouts" color="success"
          >Load More
        </v-btn>
      </div>
    </v-main>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";
export default {
  name: "MyHome",
  data() {
    return {
      workouts: [],
      user: null,
      part_of_body: null,
      workout: null,
      memo: null,
      body_items: ["CHEST", "BACK", "SHOULDER", "LEG"],
      dialog: false,
      next: null,
      loading: false,
    };
  },
  methods: {
    getWorkouts() {
      let endpoint = "api/workouts/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loading = true;
      apiService(endpoint).then((data) => {
        this.workouts.push(...data.results);
        this.loading = false;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    },
  },
  onSubmit() {
    let endpoint = "/api/workouts/";
    let method = "POST";
    apiService(endpoint, method, {
      part_of_body: this.part_of_body,
      workout: this.workout,
      memo: this.memo,
    }).then((workout_data) => {
      this.$router.push({
        name: "workout",
        params: { id: workout_data.id },
      });
    });
  },
  created() {
    this.getWorkouts();
    console.log(this.workouts);
  },
};
</script>
