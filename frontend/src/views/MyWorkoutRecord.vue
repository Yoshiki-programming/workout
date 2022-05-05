<template>
  <div>
    <v-container style="size: 150px">筋トレの記録</v-container>
    <v-row justify="space-around">
      <v-col cols="auto">
        <v-dialog transition="dialog-top-transition" max-width="600">
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="success" v-bind="attrs" v-on="on">+</v-btn>
          </template>
          <template v-slot:default="dialog">
            <v-card>
              <v-toolbar color="success" dark>記録する</v-toolbar>
              <v-divider></v-divider>
              <v-card-text style="height: 400px">
                <form @submit.prevent="onSubmit">
                  <v-text-field required v-model="weight" label="重さ">
                  </v-text-field>

                  <v-text-field
                    v-model="reps"
                    label="回数"
                    required
                  ></v-text-field>

                  <v-textarea v-model="memo" label="メモ"></v-textarea>
                  <v-btn color="success" text @click="dialog.value = false">
                    閉じる
                  </v-btn>
                  <v-btn
                    v-if="reps"
                    color="success"
                    type="submit"
                    text
                    @click="dialog.value = false"
                  >
                    保存する
                  </v-btn>
                </form>
              </v-card-text>
            </v-card>
          </template>
        </v-dialog>
      </v-col>
    </v-row>
    <v-main>
      <div v-for="record in workoutrecords" :key="record.pk">
        <h2>
          <router-link
            :to="{ name: 'RecordDetail', params: { id: record.id } }"
            class="myworkoutrecord-link"
          >
            <v-card>
              <v-card-title>
                {{ record.workout.workout }} /
                {{ record.workout.part_of_body }}</v-card-title
              >
              <v-card-text style="size: 50px"
                >{{ record.weight }} KG</v-card-text
              >
              <v-card-text style="size: 50px">{{ record.reps }} 回</v-card-text>
              <v-card-text style="size: 50px"
                >メモ：{{ record.memo }}</v-card-text
              >
              <v-card-text style="size: 50px"
                >日時：{{ record.date }}</v-card-text
              >
            </v-card>
          </router-link>
        </h2>
      </div>
      <div class="my-4">
        <p v-show="loading">...loading...</p>
        <v-btn v-show="next" @click="getWorkoutRecords" color="success"
          >もっと見る
        </v-btn>
      </div>
    </v-main>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";
export default {
  name: "MyRecord",
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
    onSubmit() {
      let endpoint = `/api/workout-records/${this.id}/`;
      let method = "POST";
      apiService(endpoint, method, {
        workout_id: this.id,
        weight: this.weight,
        reps: this.reps,
        memo: this.memo,
      }).then(
        this.$router.go({ path: this.$router.currentRoute.path, force: true })
      );
    },
  },
  created() {
    this.getWorkoutRecords();
    // console.log("record", this.workoutrecords);
    // console.log("id:", this.id);
  },
};
</script>
