<template>
  <div>
    <v-container fixed style="size: 150px">筋トレの追加、選択</v-container>
    <v-row justify="space-around">
      <v-col cols="auto">
        <v-dialog transition="dialog-top-transition" max-width="600">
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="success" v-bind="attrs" v-on="on"
              >筋トレを追加する</v-btn
            >
          </template>
          <template v-slot:default="dialog">
            <v-card>
              <v-toolbar color="success" dark>筋トレを追加する</v-toolbar>
              <v-divider></v-divider>
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
                  <v-btn color="success" text @click="dialog.value = false">
                    閉じる
                  </v-btn>
                  <v-btn
                    v-if="part_of_body && workout"
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
      <v-row justify="space-around">
        <v-col cols="auto">
          <p v-show="loading">...ローディング...</p>
          <v-btn v-show="next" @click="getWorkouts" color="success"
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
    // console.log(this.workouts);
  },
};
</script>
