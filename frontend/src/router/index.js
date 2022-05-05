import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/MyHome.vue";
import Workout from "../views/MyWorkout.vue";
import Record from "../views/MyWorkoutRecord";
import Editor from "../views/MyWorkoutEditor";
import RecordDetatail from "../views/MyRecordDetail";
import RecordEdit from "../views/MyWorkoutRecordEdit";
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
    props: (route) => ({ id: parseInt(route.params.id) }),
  },
  {
    path: "/record/:id", // 追加
    name: "MyRecord",
    component: Record,
    props: (route) => ({ id: parseInt(route.params.id) }),
  },
  {
    path: "/record-detail/:id", // 追加
    name: "RecordDetail",
    component: RecordDetatail,
    props: (route) => ({ id: parseInt(route.params.id) }),
  },
  {
    path: "/edit/:id", // 追加
    name: "MyEditor",
    component: Editor,
    props: (route) => ({ id: parseInt(route.params.id) }),
  },
  {
    path: "/record-edit/:id", // 追加
    name: "RecordEdit",
    component: RecordEdit,
    props: (route) => ({ id: parseInt(route.params.id) }),
  },
];

const router = new VueRouter({
  mode: "hash",
  routes,
});

export default router;
