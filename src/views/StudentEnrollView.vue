<template>
  <nav>
    <ul class="nav-links">
      <li>
        <RouterLink to="/student/schedule">View Schedule</RouterLink>
      </li>
      <li>
        <RouterLink to="/student/enroll">Search and Enroll</RouterLink>
      </li>
      <li>
        <RouterLink to="/">Log out</RouterLink>
      </li>
    </ul>
  </nav>
  <main class="enroll-view">
    <h2>Search and Enroll in Courses</h2>
	<h3>
		(If you do not see any courses populate, please type another character after pressing 'Search'.)
	</h3>
    <div class="search">
      <input type="text" v-model="course_search_bar" placeholder="Search for class name or title (case sensitive)" />
      <button class ="sButton" type="button" @click="getCourses" @keydown.enter="getCourses">Search</button>
      <div class="course-list" v-for="course in courseCatalog" :key="course">
        <h4>{{ course[0]+' - '+course[2]}}</h4>
		<h5>{{ 'Professor: '+course[7]+', '+course[1]+' credit(s)' }}</h5>
		<h5>{{ course[3]+'-'+course[4]+' - '+course[5] }}</h5>
		<h5>{{ 'Current enrollment: '+course[9]+'/'+course[8]+' ('+(course[8]-course[9])+' open seats)'}}</h5>
        <h5>{{ }}</h5>
		<!-- <a>{{ (course[9] != course[8] && student_credits + course[1] <= MAX_CREDITS) ? 'Enroll in course (TODO make this a buttton!!)' : 'Enrollment restricted (Seats full or maximum # credits enrolled)' }}</a> -->
		<button class ="eButton" type="button" @click="enrollStudentInCourse">Enroll in {{course[0]}}</button>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref } from "vue";
import { searchMultipleCourseCatalog, enrollStudent} from "../util/api-setup";

const course_search_bar = ref("");
var courseCatalog = []

const MAX_CREDITS = 19
/* this should get the number of credits a student has from dynamo */
var student_credits = 16

//get courses from dynamoDB courseCatalog
const getCourses = async () => {
  const { data, error } = await searchMultipleCourseCatalog(course_search_bar.value);

  if (data) {
    courseCatalog = data.courses;
    //console.log(data.courses);
  }

  if (error) {
    courseCatalog = ["There was an error, please search again."];
  }
};

//enroll student in a course
const enrollStudentInCourse = async () => {

  const studentID = "abc54321"
  const course = "SCI1010"
  const {data, error } = await enrollStudent({studentID, course});

  if (data) {
    //the following series of if statements sends values to the console,
    //these should be shown to the user as an alert or some other message
    
  if (data.body.includes("have been enrolled")) {
      console.log("You have been enrolled!!");
    } else if (data.body.includes("max capacity")){
      console.log("Course is at max capacity");
    } else if (data.body.includes("too many credits")) {
      console.log("You are enrolled in too many credits");
    } else {
      console.log("There was an error, please try again.");
    }
  } else {
    console.log(error)
  }

};


</script>
<style>
  .home {
    padding: 1rem;
  }
  
  /* page heading */
  .enroll-view h2 {
    font-size: 1.75rem;
    margin-bottom: .75rem;
	text-align: center;
	font-weight: bold;
  }
  
  /* page sub-heading */
  .enroll-view h3 {
    font-size: 1rem;
    margin-bottom: 1.5rem;
	text-align: center;
  }
  
  /* course title */
  .enroll-view h4 {
	font-weight: bold;
	text-align: center;
	/* add any params to on-screen text here*/
  }
  
  /* course descriptors */
  .enroll-view h5 {
	text-align: center;
	/* add any params to on-screen text here*/
  }
  
  /* hyperlinks (i.e. enroll button) */
  .enroll-view a {
	display: flex;
	justify-content: center;
    margin-bottom: 1.5rem;
	/* add any params to on-screen text here*/
  }

	/* search button */
  .sButton {
    height: 2rem;
    width: 8rem;
    background-color: #1212c2;
    -webkit-text-fill-color: #fef1fc;
    margin: -60rem 1rem 1.5rem 38.5rem;
  }
  
  /* enrollment button */
  .eButton {
	display: flex;
	justify-content: center;
    align-items: center;
	text-align: center;
	margin: 0.5rem 37rem 1.2rem;
    background-color: #00CC00;
    -webkit-text-fill-color: #FFFFFF;
    height: 2rem;
    width: 11rem;
  }
  
  /* enrollment failed button */
  .efButton {
	/* failed attempts to get this stupid button to center. i give up - pierson */
	display: flex;
	justify-content: center;
    align-items: center;
	text-align: center;
	margin: 0.5rem 37rem 1.2rem;
    background-color: #CCCCCC;
    -webkit-text-fill-color: #000000;
    height: 2rem;
    width: 11rem;
  }
  
  /* unenroll button */
  .ueButton {
	/* failed attempts to get this stupid button to center. i give up - pierson */
	display: flex;
	justify-content: center;
    align-items: center;
	text-align: center;
	margin: 0.5rem 37rem 1.2rem;
    background-color: #CC0000;
    -webkit-text-fill-color: #FFFFFF;
    height: 2rem;
    width: 11rem;
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