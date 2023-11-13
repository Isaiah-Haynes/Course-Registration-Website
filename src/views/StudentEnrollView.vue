<template>
  <nav>
    <ul class="nav-links">
      <li>
        <RouterLink to="/student/home">Home</RouterLink>
      </li>
      <li>
        <RouterLink to="/student/schedule">View Schedule</RouterLink>
      </li>
      <li>
        <RouterLink to="/">Log out</RouterLink>
      </li>
    </ul>
  </nav>
  <main class="enroll-view">
    <h2>Search all courses</h2>
    <p>
      This is the page for students to enroll in courses.
    </p>
    <div class="search">
      <input type="text" v-model="course_search_bar" placeholder="Search for class name or title (case sensitive)" />
      <button class ="sButton" type="button" @click="getCourses">Search</button>
      <div class="course-list" v-for="course in courseCatalog" :key="course">
        <p>{{ course }}</p>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref } from "vue";
import { searchMultipleCourseCatalog } from "../util/api-setup";

const course_search_bar = ref("");
var courseCatalog = []

//get courses from dynamoDB courseCatalog
const getCourses = async () => {
  const { data, error } = await searchMultipleCourseCatalog(course_search_bar.value);

  if (data) {
    courseCatalog = data.courses;
    console.log(data.courses);
  }

  if (error) {
    courseCatalog = ["There was an error, please search again."];
  }
};

</script>
<style>
  .home {
    padding: 1rem;
  }
  
  .home h2 {
    font-size: 1.5rem;
    margin-bottom: 2rem;
  }
  
  .home p {
    margin-bottom: 1rem;
  }

  .sButton {
    margin: 0.4px;
    height: 2rem;
    width: 8rem;
    background-color: #1212c2;
    -webkit-text-fill-color: #8eb1fc;
    margin: -60rem 1rem 0.4rem 52rem;
    align-items: right;
  }

  .enroll-view input {
    display: block;
    width: 500px;
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
</style>