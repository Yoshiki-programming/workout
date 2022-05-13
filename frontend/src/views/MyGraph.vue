<template>
  <div>
    <v-row justify="center">
      <div>トレーニングの重量と回数のグラフ</div>
    </v-row>
    <v-card class="my-5 mx-2" color="#fbfbfd" elevation="5">
      <LineChart v-if="loaded" :chart-data="chartData" :options="options" />
      <LineChart v-if="loaded" :chart-data="chartData2" :options="options2" />
    </v-card>
    <v-row justify="center">
      <v-btn
        :to="{
          name: 'MyRecord',
          params: { id: this.id },
        }"
        color="primary"
        text
        class="mx-2 my-5"
        >戻る
      </v-btn>
    </v-row>
  </div>
</template>

<script>
import LineChart from "./LineChart";
export default {
  name: "MyGraph",
  components: {
    LineChart,
  },
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  data: () => ({
    data: [],
    loaded: false,
    chartData: {
      labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
      datasets: [
        {
          label: "重量の伸び率",
          fill: false,
          tension: 0.1,
          borderColor: "rgb(75, 192, 192)",
          data: [],
        },
      ],
    },
    chartData2: {
      labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
      datasets: [
        {
          label: "回数の伸び率",
          fill: false,
          tension: 0.1,
          borderColor: "#EC407A",
          data: [],
        },
      ],
    },
    options: {
      indexAxis: "y",
      scales: {
        xAxes: [
          {
            scaleLabel: {
              display: true,
              labelString: "過去15セット()",
            },
          },
        ],
        yAxes: [
          {
            scaleLabel: {
              display: true,
              labelString: "重量(KG)",
            },
            ticks: {
              beginAtZero: true,
              stepSize: 10,
            },
          },
        ],
      },
    },
    options2: {
      indexAxis: "y",
      scales: {
        xAxes: [
          {
            scaleLabel: {
              display: true,
              labelString: "過去15セット",
            },
          },
        ],
        yAxes: [
          {
            scaleLabel: {
              display: true,
              labelString: "回数(回)",
            },
            ticks: {
              beginAtZero: true,
              stepSize: 3,
            },
          },
        ],
      },
    },
  }),
  async mounted() {
    this.loaded = false;
    try {
      const records = await fetch(`/api/workout-records/${this.id}/`);
      const json = await records.json();
      // console.log(json.results.map((obj) => obj.weight).reverse());
      this.chartData.datasets[0].data = json.results
        .map((obj) => obj.weight)
        .reverse();
      this.chartData2.datasets[0].data = json.results
        .map((obj) => obj.reps)
        .reverse();
      this.loaded = true;
    } catch (e) {
      console.error(e);
    }
  },
};
</script>
