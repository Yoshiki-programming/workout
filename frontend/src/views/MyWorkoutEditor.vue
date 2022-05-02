<template>
  <div>
    <v-container style="size: 150px">EDIT WORKOUT</v-container>
    <v-main>
      <v-row justify="center" style="">
        <v-card style="">
          <v-card-title>EDIT WORKOUT</v-card-title>
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
              <v-btn color="success" text> Close </v-btn>
              <v-btn color="success" type="submit"> Save </v-btn>
            </form>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions> </v-card-actions>
        </v-card>
      </v-row>
    </v-main>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";

export default {
  name: "WorkoutPut",
  props: {
    id: {
      type: Number,
      required: false,
    },
  },
  data() {
    return {
      workout: null,
      part_of_body: null,
      memo: null,
    };
  },
  methods: {
    onSubmit() {
      let endpoint = `/api/workout/${this.id}/`;
      let method = "PUT";
      apiService(endpoint, method, {
        workout: this.workout,
        part_of_body: this.part_of_body,
        memo: this.memo,
      }).then((workout_data) => {
        this.$router.push({
          name: "workout",
          params: { id: workout_data.id },
        });
      });
    },
  },
  async beforeRouteEnter(to, from, next) {
    if (to.params.id !== undefined) {
      let endpoint = `/api/workout/${to.params.id}/`;
      let data = await apiService(endpoint);
      return next((vm) => {
        (vm.workout = data.workout),
          (vm.part_of_body = data.part_of_body),
          (vm.memo = data.memo);
      });
    } else {
      return next();
    }
  },
  created() {
    document.title = "Edit - workout";
  },
};
</script>
