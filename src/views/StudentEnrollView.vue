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
    <h2>Student Enroll View</h2>
    <p>
      This is the page for students to enroll in courses.
    </p>
    <div class="search">
      <input type="text" v-model="search_bar" placeholder="Search for a class (enter title or name)" />
      <button class ="sButton" type="button" @click="getCourses">Search</button>
      <div class="course-list" v-for="course in courseCatalog" :key="course">
        <p>{{ course }}</p>
      </div>
    </div>
  </main>
</template>

<script>
import { ref, computed } from "vue";
let search_bar = ref("");
//const courseCatalog = ["hello"];
const data = ref();
const url = computed(
  () => 
  `https://rr0ix1pdq0.execute-api.us-east-1.amazonaws.com/finalStage/courseCatalog?tableFilter=${search_bar.value}`
)
// const url = 'https://rr0ix1pdq0.execute-api.us-east-1.amazonaws.com/testFilter/courseCatalog?tableFilter=10'

export default {
  props: {
    msg: String,
  },
  data() {
    return {
      courseCatalog: ref(""),
    };
  },
  methods: {
    getCourses() {
      fetch(url, {
        method: "POST",
        headers: {
          "content-type": "application/json",
          "x-amz-docs-region": "us-east-1",
        },
        data: {
          "tableColumn": "course_name"
        }
      })
      .then((response) => {
        response.json().then((data) => {
          this.courseCatalog = data[0];
        });
      })
      .catch((err) => {
        console.error(err);
      });
    },
  },
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