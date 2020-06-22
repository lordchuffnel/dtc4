<template>
  <div>
    <h1>Timecards</h1>
    <div v-for="timecard in timecards" :key="timecard.id" :timecard="tc">
      <ul>
        <li>{{ timecard[0].date }}</li>
        <li>{{ timecard.time }}</li>
        <li>{{ timecard.start_time }}</li>
        <li>{{ tc.date }}</li>
        <li>{{ tc.start_time }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
// import { mapState } from 'vuex';
export default {
  name: 'Timecards',
  data() {
    return {
      timecards: [],
      tc: null,
    };
  },
  methods: {
    getTimecards() {
      fetch('http://127.0.0.1:8000/api/timecards/', {
        method: 'GET',
        headers: {
          Authorization: 'Token 23936257d376bd10222b1c7329983cb437f3e356',
        },
      })
        .then((res) => res.json())
        .then((res) => {
          this.timecards = res;
          if (this.tc) {
            this.tc = this.timecards.find(
              (timecard) => timecard.id === this.tc.id
            );
          }
        })
        .catch((err) => console.log(err));
    },
  },
  created() {
    this.getTimecards();
  },
  // computed: { ...mapState(['timecards', 'user', 'loading']) },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  font-size: 40px;
}
</style>
