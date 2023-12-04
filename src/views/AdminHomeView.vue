<template>
  <div class="title-bar">
    <h2>Admin Home Page</h2>
    <!-- <RouterLink to="/">Log out</RouterLink> -->
    <LogOut />
  </div>
  <main class="home">
    <button @click="() => TogglePopup('buttonTrigger')">Open Popup</button>
    <coursePopup v-if="popupTriggers.buttonTrigger" :TogglePopup="() => TogglePopup('buttonTrigger')">
      <h2>{{ alertMsg }}</h2>
    </coursePopup>
    <div class="cards">

      <div class="card-row">
        <div class="card-title">
          <p>Manage Courses</p>
          <div class="course-actions">
            <button type="button" @click="addCourse">Add Course</button>
            <p class="action-desc">To add a course, fill in all required boxes and click 'Add Course'.</p>
            <button type="button" @click="updateCourse">Edit Course</button>
            <p class="action-desc">To edit a course, fill in the Course Name and additional changes. Then, click 'Edit Course'.</p>
            <button type="button" @click="removeCourse">Remove Course</button>
            <p class="action-desc">To remove a course, fill in the course's name and click 'Remove Course'.</p>
          </div>
        </div>
        <div class="actions">
          <form id="manage-form" class="manage-form">
            <input type="text" id="inputField" name="inputField" v-model="courseName" placeholder="Course Name *" required>
            <input type="text" id="inputField" name="inputField" v-model="numCredits" placeholder="Credits">
            <input type="text" id="inputField" name="inputField" v-model="courseTitle" placeholder="Course Title">
            <input type="text" id="inputField" name="inputField" v-model="courseStart" placeholder="Start Time">
            <input type="text" id="inputField" name="inputField" v-model="courseEnd" placeholder="End Time">
            <input type="text" id="inputField" name="inputField" v-model="courseDays" placeholder="Days">
            <input type="text" id="inputField" name="inputField" v-model="subject" placeholder="Department">
            <input type="text" id="inputField" name="inputField" v-model="professor" placeholder="Professor">
            <input type="text" id="inputField" name="inputField" v-model="maxEnrollment" placeholder="Max Enrollment">
            <input type="text" id="inputField" name="inputField" v-model="currentEnrollment" placeholder="Current Enrollment">
            <input type="text" id="inputField" name="inputField" v-model="prerequisistes" placeholder="Prerequisites">
          </form>
        </div>
      </div>
 
      <div class="card-row">
        <div class="card-title">
          <p>Manage Students</p>
          <div class="course-actions">
            <button type="button" @click="addStudentToDB">Add Student</button>
            <p class="action-desc">To add a student, fill in all required boxes and click 'Add Student'.</p>
            <button type="button" @click="updateStudent">Edit Student</button>
            <p class="action-desc">To edit a student, fill in the student's id and additional changes. Then, click 'Edit Student'.</p>
            <button type="button" @click="removeStudentFromDB">Remove Student</button>
            <p class="action-desc">To remove a student, fill in the student's id and click 'Remove Student'.</p>
          </div>
        </div>
        <div class="actions">
          <form id="manage-form" class="manage-form">
            <input type="text" id="inputField" name="inputField" v-model="studentID" placeholder="ID *" required>
            <input type="text" id="inputField" name="inputField" v-model="studentName" placeholder="Name">
            <input type="text" id="inputField" name="inputField" v-model="major" placeholder="Major">
            <input type="text" id="inputField" name="inputField" v-model="minor" placeholder="Minor">
            <input type="text" id="inputField" name="inputField" v-model="standing" placeholder="Standing">
            <input type="text" id="inputField" name="inputField" v-model="gpa" placeholder="GPA">
            <input type="text" id="inputField" name="inputField" v-model="totalCredits" placeholder="Total Credits">
            <input type="text" id="inputField" name="inputField" v-model="enrolledCredits" placeholder="Enrolled Credits">
            <input type="text" id="inputField" name="inputField" v-model="enrolledCourses" placeholder="Enrolled Courses">
            <input type="text" id="inputField" name="inputField" v-model="pastCourses" placeholder="Past Courses">
          </form>
        </div>
      </div>
 
      <div class="card-row">
        <div class="card-title">
          <p>Manage Professors</p>
          <div class="course-actions">
            <button type="button" @click="addProfessorToDB">Add Professor</button>
            <p class="action-desc">To add a professor, fill in all required boxes and click 'Add Professor'.</p>
            <button type="button" @click="updateProfessor">Edit Professor</button>
            <p class="action-desc">To edit a professor, fill in the professor's id and additional changes. Then, click 'Edit Professor'.</p>
            <button type="button" @click="removeProfessorFromDB">Remove Professor</button>
            <p class="action-desc">To remove a professor, fill in the professor's id and click 'Remove Professor'.</p>
          </div>
        </div>
        <div class="actions">
          <form id="manage-form" class="manage-form">
            <input type="text" id="inputField" name="inputField" v-model="professorID" placeholder="ID *" required>
            <input type="text" id="inputField" name="inputField" v-model="professorName" placeholder="Name">
            <input type="text" id="inputField" name="inputField" v-model="professorDept" placeholder="Department">
            <input type="text" id="inputField" name="inputField" v-model="currentCourses" placeholder="Current Courses">
          </form>
        </div>
      </div>

    </div>
  </main>
 </template>

<script setup>
import { ref } from "vue";
import { deleteCourseFromCourseCatalog, addCourseToCourseCatalog, editCourse } from "../util/api-setup";
import { addStudent, deleteStudent, editStudent } from "../util/api-setup";
import { addProfessor, deleteProfessor, editProfessor } from "../util/api-setup";
import LogOut from "@/components/buttons/logout-button.vue";
import coursePopup from "../components/course-info-popup.vue";

var alertMsg = ref("");
// functionality for course buttons
const courseName = ref("");
const numCredits = ref("");
const courseTitle = ref("");
const courseStart = ref("");
const courseEnd = ref("");
const courseDays = ref("");
const subject = ref("");
const professor = ref("");
const maxEnrollment = ref("");
const currentEnrollment = ref("");
const prerequisistes = ref("");


const addCourse = async () => {
  const { data, error } = await addCourseToCourseCatalog({
    courseName: courseName.value,
    numCredits: numCredits.value,
    courseTitle: courseTitle.value,
    courseStart: courseStart.value,
    courseEnd: courseEnd.value,
    courseDays: courseDays.value,
    subject: subject.value,
    professor: professor.value,
    maxEnrollment: maxEnrollment.value,
    currentEnrollment: currentEnrollment.value,
    prerequisistes: prerequisistes.value
  });

  if (data) {
    //choose what happens with the data returned from the api
    // console.log(data);
    if (JSON.stringify(data).includes('error')) { 
      alertMsg = "There was an error, please try again.";
      TogglePopup('buttonTrigger');
    } else {
      alertMsg = courseName.value + " has been added!!";
      TogglePopup('buttonTrigger');
      //clear input boxes
      courseName.value = '';
      numCredits.value = '';
      courseTitle.value = '';
      courseStart.value = '';
      courseEnd.value = '';
      courseDays.value = '';
      subject.value = '';
      professor.value = '';
      maxEnrollment.value = '';
      currentEnrollment.value = '';
      prerequisistes.value = '';
    };
  } else {
    //choose what happens with the error returned from the api
    // console.log(error);
    alertMsg = JSON.stringify(error);
    TogglePopup('buttonTrigger');
  }
};

const updateCourse = async () => {
  const { data, error } = await editCourse({
    courseName: courseName.value,
    numCredits: numCredits.value || "",
    courseTitle: courseTitle.value || "",
    courseStart: courseStart.value || "",
    courseEnd: courseEnd.value || "",
    courseDays: courseDays.value || "",
    subject: subject.value || "",
    professor: professor.value || "",
    maxEnrollment: maxEnrollment.value || "",
    currentEnrollment: currentEnrollment.value || "",
    prerequisistes: prerequisistes.value || ""
  })

  if (data) {
    //choose what happens with the data returned from the api
    // console.log(data);
    if (JSON.stringify(data).includes('error')) { 
      alertMsg = "There was an error, please try again.";
      TogglePopup('buttonTrigger');
    } else {
      alertMsg = courseName.value + " has been updated!!";
      TogglePopup('buttonTrigger');
      //clear input boxes
      courseName.value = '';
      numCredits.value = '';
      courseTitle.value = '';
      courseStart.value = '';
      courseEnd.value = '';
      courseDays.value = '';
      subject.value = '';
      professor.value = '';
      maxEnrollment.value = '';
      currentEnrollment.value = '';
      prerequisistes.value = '';
    }
  } else {
    //choose what happens with the error returned from the api
    // console.log(error);
    alertMsg = JSON.stringify(error);
    TogglePopup('buttonTrigger');
  }
}

const removeCourse = async () => {
  const { data, error } = await deleteCourseFromCourseCatalog(courseName.value);

  if (data) {
    //choose what happens with the data returned from the api
    // console.log(data.body);
    alertMsg = courseName.value + " has been deleted!!";
    TogglePopup('buttonTrigger');

    //clear input boxes
    courseName.value = '';
    
  } else {
    //choose what happens with the error returned from the api
    // console.log(error);
    alertMsg = JSON.stringify(error);
    TogglePopup('buttonTrigger');
  }
};

/* functionality for student buttons */

const studentID = ref("");
const studentName = ref("");
const major = ref("");
const minor = ref("");
const standing = ref("");
const gpa = ref("");
const totalCredits = ref("");
const enrolledCredits = ref("");
const enrolledCourses = ref("");
const pastCourses = ref("");

const addStudentToDB = async () => {
  const { data, error } = await addStudent({
    id: studentID.value,
    name: studentName.value,
    major: major.value,
    minor: minor.value,
    standing: standing.value,
    gpa: gpa.value,
    total_credits: totalCredits.value,
    enrolled_credits: enrolledCredits.value,
    enrolled_courses: enrolledCourses.value.split(",") || ["N/A"],
    past_courses: pastCourses.value.split(",") || ["N/A"]
  });
  console.log(enrolledCourses.value);

  if (data) {
    //choose what happens with the data returned from the api
    console.log(data.body);

    //clear input boxes
    studentID.value = '';
    studentName.value = '';
    major.value = '';
    minor.value = '';
    standing.value = '';
    gpa.value = '';
    totalCredits.value = '';
    enrolledCredits.value = '';
    enrolledCourses.value = '';
    pastCourses.value = '';
    
  } else {
    //choose what happens with the error returned from the api
    console.log(error);
  }
};

const updateStudent = async () => {
  const { data, error } = await editStudent({
    id: studentID.value,
    major: major.value || "",
    minor: minor.value || "",
    standing: standing.value || "",
    gpa: gpa.value || "",
    total_credits: totalCredits.value || "",
    enrolled_credits: enrolledCredits.value || "",
    enrolled_courses: enrolledCourses.value.split(",") || [],
    past_courses: pastCourses.value.split(",") || []
  });

  if (data) {
    //choose what happens with data, should be shown to user
    // console.log(data);

    alertMsg = "Student has been updated!!";
    TogglePopup('buttonTrigger');
    //clear input boxes
    studentID.value = '';
    studentName.value = '';
    major.value = '';
    minor.value = '';
    standing.value = '';
    gpa.value = '';
    totalCredits.value = '';
    enrolledCredits.value = '';
    enrolledCourses.value = '';
    pastCourses.value = '';
  } else {
    //choose what happens with data, should be shown to user
    // console.log(error);

    alertMsg = error;
    TogglePopup('buttonTrigger');
  }
}
const removeStudentFromDB = async () => {
  const { data, error } = await deleteStudent(studentID.value);

  if (data) {
    //choose what happens with the data returned from the api
    console.log(data);
    
    //clear input box
    studentID.value = '';
    
  } else {
    //choose what happens with the error returned from the api
    console.log(error);
  }
};

/* functionality for professor buttons */

const professorID = ref("");
const professorName = ref("");
const professorDept = ref("");
const currentCourses = ref("");

const addProfessorToDB = async () => {
  const { data, error } = await addProfessor({
    id: professorID.value,
    name: professorName.value,
    department: professorDept.value,
    currentCourses: currentCourses.value.split(",") || []
  });

  if (data) {
    console.log(data);

    professorID.value = '';
    professorName.value = '';
    professorDept.value = '';
    currentCourses.value = '';
  } else {
    console.log(error);
  }
};

const updateProfessor = async () => {
  const { data, error } = await editProfessor({
    id: professorID.value,
    department: professorDept.value || "",
    currentCourses: currentCourses.value.split(",") || []
  });

  if (data) {
    console.log(data);

    professorID.value = '';
    professorName.value = '';
    professorDept.value = '';
    currentCourses.value = '';
  } else {
    console.log(error);
  }
};

const removeProfessorFromDB = async () => {
  const { data, error } = await deleteProfessor(professorID.value);

  if (data) {
    console.log(data);

    professorID.value = '';
  } else {
    console.log(error);
  }
};

const popupTriggers = ref({
  buttonTrigger: false
});

const TogglePopup = (trigger) => {
  popupTriggers.value[trigger] = !popupTriggers.value[trigger]
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
 
  .title-bar {
    display: flex;
    justify-content: space-between;
    margin: 2rem;
  }
 
  .cards {
    display: flex;
    justify-content: space-around;
    flex-direction: column;
  }
 
  .card-row {
    display: flex;
  }
 
  .card-title {
    background-color: #739ad4;
    width: 25%;
    height: 28rem;
    border-radius: 0.4rem;
    margin: 1rem;
    padding: 0.8rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    font-size: 1.2rem;
    -webkit-text-fill-color: #fafcff;
  }

  .action-desc {
    font-size: 0.8rem;
    margin: 0.4rem;
    display: flex;
    width: 75%;
  }
 
  .course-actions {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
  }

  .manage-form {
    width: 95%;
    height: 80%;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    row-gap: 4px;
    -webkit-text-fill-color: #3e71dc;
  }

  .manage-form input {
    height: 3rem;
  }

  .actions {
    background-color: #fafcff;
    width: 70%;
    height: 28rem;
    border-radius: 0.4rem;
    margin: 1rem;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    font-size: 1.2rem;
    -webkit-text-fill-color: #3e71dc;
  }

  button[type="button"] {
    background: #fafcff;
    width: 12rem;
    height: 2rem;
    padding: 0.8rem;
    border-radius: 0.4rem;
    -webkit-text-fill-color: #3e71dc;
    font-size: 0.8rem;
    display: flex;
    align-items: center;
    justify-content: center;
  }
 
 
  </style>