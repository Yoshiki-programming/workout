<template>
  <div>
    <v-row justify="space-around">
      <v-col cols="auto">
        <v-dialog transition="dialog-top-transition" max-width="600">
          <template v-slot:activator="{ on, attrs }">
            <v-row justify="center">
              <v-col>
                <v-btn color="primary" :to="{ name: 'workout' }" text
                  >戻る</v-btn
                >
              </v-col>
              <v-col>
                <v-btn color="primary" v-bind="attrs" v-on="on">追加</v-btn>
              </v-col>
              <v-col>
                <v-btn
                  v-if="workoutrecords[0]"
                  color="primary"
                  :to="{
                    name: 'MyGraph',
                    params: { id: workoutrecords[0].workout.id },
                  }"
                  >グラフ</v-btn
                >
              </v-col>
            </v-row>
            <v-row justify="center" class="my-5">
              <div v-if="workoutrecords[0]">
                {{ workoutrecords[0].workout.workout }}の記録
              </div>
            </v-row>
          </template>
          <template v-slot:default="dialog">
            <v-card>
              <v-toolbar color="#1D1DF" dark>記録</v-toolbar>
              <v-card-text style="height: 400px">
                <form @submit.prevent="onSubmit">
                  <v-text-field v-model="weight" label="重量"> </v-text-field>

                  <v-text-field
                    v-model="reps"
                    label="回数"
                    required
                  ></v-text-field>

                  <v-textarea v-model="memo" label="メモ"></v-textarea>
                  <v-btn color="primary" @click="dialog.value = false" text>
                    閉じる
                  </v-btn>
                  <v-btn
                    v-if="reps"
                    color="primary"
                    type="submit"
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
      <div v-if="workoutrecords[0]">
        <div v-for="record in workoutrecords" :key="record.pk">
          <h2>
            <router-link
              :to="{ name: 'RecordDetail', params: { id: record.id } }"
              class="myworkoutrecord-link"
            >
              <v-card class="my-5 mx-2" color="#fbfbfd" elevation="10">
                <v-card-title style="size: 50px"
                  >{{ record.weight }} KG</v-card-title
                >
                <v-card-text style="size: 50px"
                  >{{ record.reps }} 回</v-card-text
                >
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
      </div>
      <div v-else>
        <v-container class="text-center">記録はまだありません。</v-container>
      </div>
      <v-row justify="space-around">
        <v-col cols="auto">
          <p v-show="loading">...loading...</p>
          <v-btn v-show="next" @click="getWorkoutRecords" color="primary" text
            >もっと見る
          </v-btn>
        </v-col>
      </v-row>
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
