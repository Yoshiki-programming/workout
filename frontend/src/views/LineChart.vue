<script>
import { Line, mixins } from "vue-chartjs";
const { reactiveProp } = mixins;
export default {
  extends: Line,
  mixins: [reactiveProp],
  props: {
    chartData: {
      type: Object,
      required: true,
    },
    options: {
      type: Object,
      default: () => {},
    },
  },
  mounted() {
    console.log(this.chartData);
    // console.log(this.options);
    this.renderChart(this.chartData, this.options);
  },
};
</script>
