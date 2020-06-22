<template>
  <div>
    <h1>Timecards</h1>
    <div  v-for="timecard in timecards"
          :key="timecard.id">
      <ul>
        <li>{{ timecard.date }}</li>
        <li>{{ timecard.user }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Timecards",
  data() {
    return {
      timecards: [],
      tc: null
    };
  },
  methods: {
    getTimecards: function() {
      axios.get("http://127.0.0.1:8000/api/timecards/").then(res => {
        this.timecards = res.data;
      });
    }
  },
  created() {
    this.getTimecards();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  font-size: 40px;
}
</style>
