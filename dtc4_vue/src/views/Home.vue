<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <Timecards />
  </div>
</template>

<script>
// @ is an alias to /src
import Timecards from '../components/Timecards.vue'

export default {
  name: 'Home',
  components: {
    Timecards
  }
}
</script>
