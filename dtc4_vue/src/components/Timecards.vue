<template>
  <div>
    <button @click="logout()">Logout</button>
    <h1>Timecards</h1>
    <div :token="this.token" class="layout">
      <Item
        v-for="timecard in timecards"
        :key="timecard.id"
        :timecard="timecard"
        @timecard-clicked="timecardClicked($event)"
      />
    </div>
    <Details :timecard="selectedTimecard" />
  </div>
</template>

<script>
import Item from '../components/Item.vue';
import Details from '../components/Details.vue';
export default {
  name: 'Timecards',
  components: {
    Item,
    Details,
  },
  data() {
    return {
      timecards: [],
      tc: null,
      token: '',
      selectedTimecard: null,
    };
  },
  methods: {
    getTimecards: function() {
      this.$store.dispatch('getTimecards', true).then(() => {
        this.timecards = this.$store.state.timecards;
      });
    },
    timecardClicked(event) {
      this.selectedTimecard = this.timecards.find(
        (timecard) => timecard.id === event.id
      );
    },
    logout() {
      this.$cookies.remove('dtc4-token');
      this.$router.push('/auth');
    },
  },
  mounted() {
    if (this.$cookies.isKey('dtc4-token')) {
      this.token = this.$cookies.get('dtc4-token');
      this.getTimecards();
    } else {
      this.$router.push('/auth');
    }
  },
  created() {
    // this.getTimecards();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  font-size: 40px;
}
.layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
}
</style>
