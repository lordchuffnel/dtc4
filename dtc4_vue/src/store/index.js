import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    timecards: [],
    user: null,
    loading: false,
    timecard: {},
  },
  mutations: {
    setTimecardInfo: (state, el) => {
      state.timecards = el;
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
    getTimecards: function({ commit, state }, force) {
      if (state.timecards.length && !force) {
        return state.timecards;
      }
      axios.get('http://127.0.0.1:8000/api/timecards/').then((res) => {
        if (res && res.data) {
          commit('setTimecardInfo', res.data);
        }
      });
    },
  },
  modules: {},
});
