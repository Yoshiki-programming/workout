<template>
  <div>
    <v-container style="size: 150px">
      <form @submit.prevent="onSubmit">
        <v-text-field v-model="weight" label="重さ"> </v-text-field>

        <v-text-field v-model="reps" label="回数" required></v-text-field>

        <v-textarea v-model="memo" label="メモ"></v-textarea>
        <v-btn
          color="primary"
          :to="{ name: 'RecordDetail', params: { id: this.id } }"
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
  name: "RecordEdit",
  props: {
    id: {
      type: Number,
      required: false,
    },
  },
  data() {
    return {
      workout: null,
      weight: null,
      reps: null,
      memo: null,
    };
  },
  methods: {
    onSubmit() {
      let endpoint = `/api/workout-records/${this.id}/record/`;
      let method = "PUT";
      apiService(endpoint, method, {
        weight: this.weight,
        reps: this.reps,
        memo: this.memo,
      }).then(() => {
        this.$router.push({
          name: "home",
        });
      });
    },
  },
  async beforeRouteEnter(to, from, next) {
    if (to.params.id !== undefined) {
      let endpoint = `/api/workout-records/${to.params.id}/record/`;
      let data = await apiService(endpoint);
      return next((vm) => {
        (vm.workout = data.workout),
          (vm.weight = data.weight),
          (vm.reps = data.reps),
          (vm.memo = data.memo);
      });
    } else {
      return next();
    }
  },
  created() {
    document.title = "記録 - 編集";
  },
};
</script>
