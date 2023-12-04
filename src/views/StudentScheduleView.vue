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
        <!-- <RouterLink to="/">Log out</RouterLink> -->
        <LogOut />
      </li>
    </ul>
  </nav>
    <main class="schedule-view">
      <popup v-if="popupTriggers.buttonTrigger" :TogglePopup="() => TogglePopup('buttonTrigger')">
        <h2>{{ alertMsg }}</h2>
      </popup>
      <h2>Welcome back!</h2>
      <h3>Enter you student ID and press "View Schedule" twice to see your schedule.</h3>
      <h3>If you enter the wrong ID, please reload the page and try again.</h3>
	  <div class="schedule">
      <input type="text" name="searchBar" v-model="studentID_input" placeholder="Enter your studentID" />
      <button class ="sButton" type="button" @click="studentInfo" @keydown.enter="studentInfo">View Schedule</button>
      <courseEntry v-if="!popupTriggers.courseAvailable">
      </courseEntry>
      <div class="course-list" v-for="course in schedule" :key="course">
        <h4>{{ course[0]+' - '+course[2]}}</h4>
        <h5>{{ 'Professor: '+course[7]+', '+course[1]+' credit(s)' }}</h5>
        <h5>{{ course[3]+'-'+course[4]+' - '+course[5] }}</h5>
        <h5>{{ 'Current enrollment: '+course[9]+'/'+course[8]+' ('+(course[8]-course[9])+' open seats)'}}</h5>
        <h5>{{ }}</h5>
        <button class ="ueButton" type="button" @click="unenrollStudentFromCourse(course[0])">Unenroll from {{course[0]}}</button>
      </div>
    </div>
    </main>
  </template>

<script setup>
import { ref } from "vue";
import { getStudentInfo, unenrollStudent, searchMultipleCourseCatalog} from "../util/api-setup";
import LogOut from "@/components/buttons/logout-button.vue";
import popup from "@/components/course-info-popup.vue";
import courseEntry from "@/components/course-snippet.vue";

var alertMsg = ref("");

// testing student id -- CHANGE LATER
// const studentID = "abc12345"
const studentID_input = ref("");
// const studentID = studentID_input.value;
var student_info = []
var schedule = []


// const inputStudentID = ref("");
// get student info from dynamoDB "students" table
const studentInfo = async () => {
  const { data, error } = await getStudentInfo(studentID_input.value);
  // console.log(studentID_input.value)
  if (data) {
    student_info = data.student;
	if (schedule.length == 0){
		//console.log("student_info[8]")
		//console.log(student_info[8])
    // "course" var here appears as a number for some reason
		for(let course in student_info[8]){
			//console.log(student_info[8][course])
      // iterate through list of enrolled courses and get info from DB
			getCourses(student_info[8][course])
		}
	}
	//console.log("studentInfo() completed p2")
	// console.log("got student schedule")
	// console.log(schedule)
  // console.log(popupTriggers.value);
  TogglePopup('courseAvailable');
  // console.log(popupTriggers.value);
  

  }

  if (error) {
    student_info = ["There was an error getting student info, please try again."];
  }
};

// get info for a course
const getCourses = async (course_name) => {
	//console.log("calling getCourses on:")
	//console.log(course_name)
  const { data, error } = await searchMultipleCourseCatalog(course_name);

  if (data) {
    //console.log(data.courses[0])
    //console.log(schedule)
    //console.log(schedule.includes(data.courses[0]))
    // in theory this should fix duplicate course adds that come from spamming the button
    // however, this does not work at the moment
    if (schedule.includes(data.courses[0]) == false) {
      if (data.courses[0] != undefined) {
        schedule.push(data.courses[0]);
      }
    // schedule.push(data.courses[0])
    }
	// console.log("Got course:")
	// console.log(data.courses[0])
	// console.log("getCourses() completed")
  }

  if (error) {
    schedule = ["There was an error, please search again."];
  }
};

// unenroll student from course
const unenrollStudentFromCourse = async (course) => {
  console.log("Attempting to unenroll from " + course)
  const studentID = studentID_input.value;
  const {data, error} = await unenrollStudent({studentID, course});

  if (data) {
    // Possible Outputs:
	// "Unenroll SUCCESSFUL - You have been unenrolled!"
	// "Unenroll FAILED - You are not enrolled in this course!" (course not in student[enrolled_courses])
	console.log(data.body);
  if (JSON.stringify(data.body).includes('SUCCESSFUL')) {
    alertMsg = "You have successfully unenrolled from " + course;
  } else if (JSON.stringify(data.body).includes('Unenroll FAILED')) {
    alertMSG = "You cannot unenroll from a course you are not enrolled in";
  } else {
    alertMsg = "There was an error, please try again.";
  }
  TogglePopup('buttonTrigger');

  } else {
    console.log(error);
    alertMsg = "There was an error, please try again.";
    TogglePopup('buttonTrigger');
  }

};

//following used to check status for reactive components.
const popupTriggers = ref({
  buttonTrigger: false,
  courseAvailable: false
});

const TogglePopup = (trigger) => {
  popupTriggers.value[trigger] = !popupTriggers.value[trigger]
};

</script>

  <style>
  .home {
    padding: 1rem;
  }
  
  .schedule-view h2 {
    font-size: 1.75rem;
    margin-bottom: .75rem;
	text-align: center;
	font-weight: bold;
  }
  
  .schedule-view h3 {
    font-size: 1rem;
    margin-bottom: 1.5rem;
	text-align: center;
  }
  
  /* course title */
  .schedule-view h4 {
	font-weight: bold;
	text-align: center;
	/* add any extra params to on-screen text here*/
  }
  
  /* course descriptors */
  .schedule-view h5 {
	text-align: center;
	/* add any extra params to on-screen text here*/
  }
  
  .schedule-view p {
    margin-bottom: 1rem;
	text-align: center;
  }

	/* centers the schedule button */
  .schedule {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

	/* search button */
  .sButton {
    height: 2rem;
    width: 8rem;
    background-color: #1212c2;
    -webkit-text-fill-color: #fef1fc;
    margin: 0rem 0rem 1rem 0rem;
  }

	/* centers the unenrollment buttons */
  .course-list {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
	/* unenroll button */
  .ueButton {
    background-color: #CC0000;	/* red */
    -webkit-text-fill-color: #FFFFFF;	/* white */
    height: 2rem;
    width: 11rem;
    margin: .5rem 0rem 1rem 0rem;
  }
  </style>
  