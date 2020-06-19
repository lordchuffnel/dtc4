<template>
  <div id="app">
    <h1>Hello world</h1>
    <Timecards />
  </div>
</template>

<script>
import Timecards from '../src/components/Timecards.vue';

export default {
  name: 'Home',
  components: {
    Timecards,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
