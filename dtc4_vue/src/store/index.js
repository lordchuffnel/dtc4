import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    timecards: [],
    user: null,
    loading: false,
  },
  mutations: {
    getTimecard: (state, el) => {
      state.timecards.map({ ...el });
    },
    addTimecard: (state, timecard) => {
      state.timecards.push(timecard);
    },
    removeTimecard: (state, timecard) => {
      state.timecards.remove(timecard);
    },
    setUser: (state, user) => {
      state.user = user;
    },
    setLoading: (state, bool) => {
      state.loading = bool;
    },
  },
  actions: {
    getTimecardInfo() {
      axios
        .get('http://127.0.0.1:8000/api/timecards/', {
          username: 'frank',
          password: 'alleyrat'
        })
        .then((res) => res.json())
        .then(res => {
          this.timecards = res;
          console.log(res)
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  modules: {},
});
