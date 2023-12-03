<template>
    <div class="course-snippet">
        <div class="course-snippet__container" v-for="course in schedule" :key="course">
            <h4>{{ course[0]+' - '+course[2]}}</h4>
            <h5>{{ 'Professor: '+course[7]+', '+course[1]+' credit(s)' }}</h5>
            <h5>{{ course[3]+'-'+course[4]+' - '+course[5] }}</h5>
            <h5>{{ 'Current enrollment: '+course[9]+'/'+course[8]+' ('+(course[8]-course[9])+' open seats)'}}</h5>
            <h5>{{ }}</h5>
            <button class ="ueButton" type="button" @click="unenrollStudentFromCourse(course[0], studentID)">Unenroll from {{course[0]}}</button>
        </div>
    </div>
  </template>
  
<script setup>
import { getStudentInfo, unenrollStudent, searchMultipleCourseCatalog} from "../util/api-setup";
// import { ref } from "vue";

// testing student id -- CHANGE LATER
const studentID = "abc54321"
var student_info = [];
var schedule = [];

// get student info from dynamoDB "students" table
const studentInfo = async () => {
  const { data, error } = await getStudentInfo(studentID);

  if (data) {
    student_info = data.student;
	if (schedule.length == 0){
		for(let course in student_info[8]){
			getCourses(student_info[8][course]);
		}
	}
	//console.log("studentInfo() completed p2")
  console.log(schedule);
	console.log("got student schedule");
	// console.log(schedule)
  }

  if (error) {
    student_info = ["There was an error getting student info, please try again."];
  }
};
// studentInfo();
// get info for a course
const getCourses = async (course_name) => {
  const { data, error } = await searchMultipleCourseCatalog(course_name);

  if (data) {
    if (schedule.includes(data.courses[0]) == false) {
    schedule.push(data.courses[0]);
    }
  }

  if (error) {
    schedule = ["There was an error, please search again."];
  }
};
const unenrollStudentFromCourse = async (course, studentID) => {
  console.log("Attempting to unenroll from " + course)
  const {data, error} = await unenrollStudent({studentID, course});

  if (data) {
	console.log(data.body);
  } else {
    console.log(error);
  }

};
studentInfo();
</script>