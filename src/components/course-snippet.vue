<template>
    <div class="course-snippet">
        <div class="course-snippet__container" v-for="course in schedule" :key="course">
          <slot />
        </div>
    </div>
  </template>
  
<script>

</script>