<template>
  <div>
    <v-container style="size: 150px">
      <form @submit.prevent="onSubmit">
        <v-select v-model="part_of_body" label="部位" :items="body_items">
        </v-select>

        <v-text-field
          v-model="workout"
          label="メニュー"
          required
        ></v-text-field>

        <v-textarea v-model="memo" label="メモ"></v-textarea>
        <v-btn
          color="primary"
          :to="{ name: 'workout', params: { id: this.id } }"
          text
          >戻る</v-btn
        >
        <v-btn color="primary" type="submit">保存</v-btn>
      </form>
    </v-container>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";

export default {
  name: "MyEditor",
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
      body_items: ["腹筋", "腕", "背中", "胸", "脚", "肩"],
    };
  },
  methods: {
    onSubmit() {
      let endpoint = `/api/workouts/${this.id}/`;
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
      let endpoint = `/api/workouts/${to.params.id}/`;
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
