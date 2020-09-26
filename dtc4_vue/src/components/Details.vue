<template>
  <div v-if="timecard">
    <h2>{{ timecard.user }}</h2>
    <p>{{ timecard.start_time }}</p>
  </div>
</template>

<script>
export default {
  name: 'Details',
  props: ['timecard'],
};
</script>
