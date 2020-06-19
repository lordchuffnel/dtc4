<template>
  <div>
    <h1>Timecards</h1>
    <div v-for="timecard in timecards" :key="timecard.id" :timecard="timecard">
      <!-- <ul>
        <li>{{ timecard.date }}</li>
        <li>{{ ttimecard.start_time }}</li>
      </ul> -->
    </div>
  </div>
</template>

<script>
import {  mapState } from 'vuex';
export default {
  name: 'Timecards',
  data() {
    return {
      timecards: [],
      tc: null
    };
  },
  methods: {
    getMovies() {
      fetch('http://127.0.0.1:8000/api/timecards/', {
        method: 'GET',
        headers: {
          username: 'frank',
          password: 'alleyrat'
        },
      }).then(res => res.json())
      .then(res => {
        this.tc = res;
      })
    }
  },
  computed: { ...mapState(['timecards', 'user', 'loading']) },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  font-size: 40px;
}
</style>
