<template>
    <header class="app-header">
      <div class="course-bar">
        <h1>{{ title }}</h1>
      </div>
    </header>
  </template>
  
  <script setup>
  // import the <RouterLink> component so that we can use it in the template above
  import { RouterLink } from "vue-router";
  
  // give this component a title property so that the parent component (app.vue) can set whatever title it wants
  defineProps({
    title: {
      type: String,
      required: true,
    },
  });
  </script>
  
  <style>
  /* give the header itself a background color, a border, and add some padding to the content */
  .app-header {
    background-color: #fcfcfc;
    padding: 1rem;
    height: 8vh;
  }
  
  /* make the title within the header a larger and bolder font */
  .app-header h1 {
    font-size: 1.2rem;
    font-weight: bold;
  }

  .course-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 100%;
    width: 100%;

  }


  </style>
  