<template>
  <div>
    <v-row justify="space-around">
      <v-col cols="auto">
        <v-dialog transition="dialog-top-transition" max-width="600">
          <template v-slot:activator="{ on, attrs }">
            <v-row justify="center" class="my-1">
              <h3>
                <p>{{ user_list.username }}さん、こんにちは！</p>
              </h3>
            </v-row>
            <v-row justify="center" class="my-5">
              <v-btn color="primary" v-bind="attrs" v-on="on">追加</v-btn>
            </v-row>
            <v-row>
              <div>トレーニングメニューの追加</div>
            </v-row>
          </template>
          <template v-slot:default="dialog">
            <v-card>
              <v-toolbar color="#1D1DF" dark>追加</v-toolbar>
              <v-card-text style="height: 400px">
                <form @submit.prevent="onSubmit">
                  <v-select
                    required
                    v-model="part_of_body"
                    label="部位"
                    :items="body_items"
                  >
                  </v-select>

                  <v-text-field
                    v-model="workout"
                    label="メニュー"
                    required
                  ></v-text-field>

                  <v-textarea v-model="memo" label="メモ"></v-textarea>
                  <v-btn color="primary" @click="dialog.value = false" text>
                    戻る
                  </v-btn>
                  <v-btn
                    v-if="part_of_body && workout"
                    color="primary"
                    type="submit"
                    @click="dialog.value = false"
                  >
                    保存
                  </v-btn>
                </form>
              </v-card-text>
            </v-card>
          </template>
        </v-dialog>
      </v-col>
    </v-row>
    <v-main>
      <div v-for="workout in workouts" :key="workout.pk">
        <h2>
          <router-link
            :to="{ name: 'workout', params: { id: workout.id } }"
            class="workout-link"
          >
            <v-card class="my-5 mx-3" color="#fbfbfd" elevation="10">
              <v-card-title> {{ workout.part_of_body }}</v-card-title>
              <v-card-text style="size: 100px">{{
                workout.workout
              }}</v-card-text>
            </v-card>
          </router-link>
        </h2>
      </div>
      <v-row justify="space-around">
        <v-col cols="auto">
          <p v-show="loading">...ローディング...</p>
          <v-btn v-show="next" @click="getWorkouts" color="primary" text
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
  name: "MyHome",
  data() {
    return {
      workouts: [],
      user_list: {},
      user: null,
      part_of_body: null,
      workout: null,
      memo: null,
      body_items: ["腹", "腕", "背中", "胸", "脚", "肩"],
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
    getUser() {
      let endpoint = "api/user/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loading = true;
      apiService(endpoint).then((data) => {
        this.user_list = data.results[0];
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    },
    onSubmit() {
      let endpoint = "/api/workouts/";
      let method = "POST";
      apiService(endpoint, method, {
        part_of_body: this.part_of_body,
        workout: this.workout,
        memo: this.memo,
      }).then(
        this.$router.go({ path: this.$router.currentRoute.path, force: true })
      );
    },
  },

  created() {
    this.getWorkouts();
    this.getUser();
    // console.log(this.workouts);
  },
};
</script>
