import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/MyHome.vue";
import Workout from "../views/MyWorkout.vue";
import Record from "../views/MyWorkoutRecord";
import Editor from "../views/MyWorkoutEditor";
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/workout/:id", // 追加
    name: "workout",
    component: Workout,
    props: true,
  },
  {
    path: "/workout-records", // 追加
    name: "WorkoutRecord",
    component: Record,
  },
  {
    path: "editor/:id", // 追加
    name: "editor",
    component: Editor,
    props: true,
  },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

export default router;
