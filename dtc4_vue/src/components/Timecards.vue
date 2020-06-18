<template>
  <div class="hello">
    <h1>Timecards</h1>
    <div v-for="(t, i) in timecards" :key="i">
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
  methods: {
    ...mapActions(['getTimecardInfo']),
  },
  computed: { ...mapState(['timecards', 'user', 'loading']) },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
