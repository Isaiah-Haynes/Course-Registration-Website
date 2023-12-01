<template>
  <nav>
    <ul class="nav-links">
      <li>
        <RouterLink to="/professor/schedule">View Schedule</RouterLink>
      </li>
      <li>
        <!-- <RouterLink to="/">Log out</RouterLink> -->
        <LogOut />
      </li>
    </ul>
  </nav>
    <main class="schedule-view">
      <h2>Welcome back!</h2>
      <h3>
        You can use this page to view your schedule.
      </h3>
	  <div class="schedule">
      <button class ="sButton" type="button" @click="professorInfo" @keydown.enter="professorInfo">View Schedule</button>
      <div class="course-list" v-for="course in schedule" :key="course">
        <h4>{{ course[0]+' - '+course[2]}}</h4>
        <h5>{{ 'Professor: '+course[7]+', '+course[1]+' credit(s)' }}</h5>
        <h5>{{ course[3]+'-'+course[4]+' - '+course[5] }}</h5>
        <h5>{{ 'Current enrollment: '+course[9]+'/'+course[8]+' ('+(course[8]-course[9])+' open seats)'}}</h5>
        <h5>{{ }}</h5>
      </div>
    </div>
    </main>
  </template>

<script setup>
import {searchMultipleCourseCatalog, getProfessorInfo} from "../util/api-setup";
import LogOut from "@/components/buttons/logout-button.vue";

// testing professor id -- CHANGE LATER
const profID = "ljs23001"
var prof_info = []
var schedule = []

// get professor info from dynamoDB "professors" table
const professorInfo = async () => {
  const { data, error } = await getProfessorInfo(profID);

  if (data) {
    prof_info = data.professor;
	if (schedule.length == 0){
		//console.log("prof_info[8]")
		//console.log(prof_info[8])
    // "course" var here appears as a number for some reason
		for(let course in prof_info[3]){
			//console.log(prof_info[8][course])
      // iterate through list of enrolled courses and get info from DB
			getCourses(prof_info[3][course])
		}
	}
	//console.log("professorInfo() completed p2")
	console.log("got professor schedule")
	console.log(schedule)
  }

  if (error) {
    prof_info = ["There was an error getting your information, please try again."];
  }
};

// get info for a course
const getCourses = async (course_name) => {
	//console.log("calling getCourses on:")
	//console.log(course_name)
  const { data, error } = await searchMultipleCourseCatalog(course_name);

  if (data) {
    console.log(data.courses[0])
    console.log(schedule)
    console.log(schedule.includes(data.courses[0]))
    // in theory this should fix duplicate course adds that come from spamming the button
    // however, this does not work at the moment
    if (schedule.includes(data.courses[0]) == false) {
    schedule.push(data.courses[0]);
    }
	//console.log("Got course:")
	//console.log(data.courses[0])
	//console.log("getCourses() completed")
  }

  if (error) {
    schedule = ["There was an error, please search again."];
  }
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
  