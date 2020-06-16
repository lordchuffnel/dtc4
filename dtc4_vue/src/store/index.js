import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    timecards: [],
    user: null,
    loading: false
  },
  mutations: {
    AddTimecard: (state, timecard) => {
      state.timecards.push(timecard)
    },
    RemoveTimecard: (state, timecard) => {
      state.timecards.remove(timecard)
    },
    SetUser: (state, user) => {
      state.user = user
    },
    SetLoading: (state, bool) => {
      state.loading = bool
    }
  },
  actions: {
    getTimecardInfo({ state, commit }) {
      axios
        .get('127.0.0.1:8000/api/timecards/')
        .then(res => res.data)
        .then(el => {
          timecard.id === el.id
          commit()
      })
    }
  },
  modules: {
  }
})
