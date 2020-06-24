<template>
  <div>
    <button @click="logout()">Logout</button>
    <h1>Timecards</h1>
    <div v-for="timecard in timecards" :key="timecard.id" :token="this.token">
      <ul>
        <li>{{ timecard.date }}</li>
        <li>{{ timecard.user }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Timecards',
  data() {
    return {
      timecards: [],
      tc: null,
      token: '',
    };
  },
  methods: {
    getTimecards: function() {
      const options = {
        headers: { Authorization: `Token ${this.token}` },
      };
      axios.get('http://127.0.0.1:8000/api/timecards/', options).then((res) => {
        this.timecards = res.data;
      });
    },
    logout() {
      this.$cookies.remove('dtc4-token');
      this.$router.push('/auth');
    },
  },

  created() {
    if (this.$cookies.isKey('dtc4-token')) {
      this.token = this.$cookies.get('dtc4-token');
      this.getTimecards();
    } else {
      this.$router.push('/auth');
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  font-size: 40px;
}
</style>
