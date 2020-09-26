import Vue from 'vue';
import VueRouter from 'vue-router';
import Timecards from '../components/Timecards.vue';
import Auth from '../components/Auth.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Timecards',
    component: Timecards,
  },
  {
    path: '/auth',
    name: 'Auth',
    component: Auth,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
