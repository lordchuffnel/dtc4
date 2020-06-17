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
        getTimecard: (state, el) => {
          state.timecards = el.data
        },
        addTimecard: (state, timecard) => {
          state.timecards.push(timecard)
        },
        removeTimecard: (state, timecard) => {
          state.timecards.remove(timecard)
        },
        setUser: (state, user) => {
          state.user = user
        },
        setLoading: (state, bool) => {
          state.loading = bool
        }
      },
      actions: {
        getTimecardInfo({
          commit
        }) {
          axios
            .get('127.0.0.1:8000/api/timecards/')
            .then((res) => res.data)
            .then(el => {
              commit('getTimecard', el)
            })
        },
        modules: {}
      }
    })