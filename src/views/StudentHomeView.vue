<template>
    <main class="quickSearchForm">
        <input type="text" v-model="search_bar" placeholder="Search for a class" />
        <div class="course name" v-for="course in filteredCatalog()" :key="course">
        <p>{{ course }}</p>
        </div>
        <div class="item error" v-if="search_bar&&!filteredCatalog().length">
        <p>No results found!</p>
        </div>
    </main>
</template>

<script setup>
import { ref } from "vue";
let search_bar = ref("");
const courseCatalog = ["CSE1000", "CSE1002", "CSE1010"];
function filteredCatalog(){
    return courseCatalog.filter((course) =>
    course.toLowerCase().includes(search_bar.value.toLowerCase())
    );
}
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Montserrat&display=swap");

* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  font-family: "Montserrat", sans-serif;
}

body {
  padding: 20px;
  min-height: 100vh;
  background-color: rgb(234, 242, 255);
}

input {
  display: block;
  width: 350px;
  margin: 20px auto;
  padding: 10px 45px;
  /* background: white url("assets/searchIcon.svg") no-repeat 15px center; */
  background-size: 15px 15px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
}

.item {
  width: 350px;
  margin: 0 auto 10px auto;
  padding: 10px 20px;
  color: white;
  border-radius: 5px;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 1px 3px 0px,
    rgba(0, 0, 0, 0.06) 0px 1px 2px 0px;
}

.course {
  background-color: rgb(255, 255, 255);
  cursor: pointer;
}

.quickSearchForm {
    padding: 1rem;
    height: 36rem;
    width: 28rem;
    display: flex;
    flex-direction: column;
    background: #fefeff;
    border: none;
    box-shadow: 0px 0px 12px 0.8px #8682ce;
    margin: 75px;
    border-radius: 1rem;
  }
.error {
  background-color: tomato;
}
</style>