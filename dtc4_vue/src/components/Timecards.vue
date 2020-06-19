<template>
  <div>
    <h1>Timecards</h1>
    <div v-for="timecard in timecards" :key="timecard.id">
      <ul>
        <li>{{ t.date }}</li>
        <li>{{ t.start_time }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';
export default {
  name: 'Timecards',
  data() {
    return {
      timecards: [],
    };
  },
  methods: {
    ...mapActions(['getTimecardInfo']),
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
