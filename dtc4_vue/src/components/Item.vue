<template>
  <div>
    <h2 @click="$emit('timecard-clicked', timecard.id)">{{ timecard.user }}</h2>
  </div>
</template>

<script>
export default {
  name: 'Item',
  props: ['timecard'],
};
</script>

<style scoped>
h2 {
  cursor: pointer;
}
</style>
