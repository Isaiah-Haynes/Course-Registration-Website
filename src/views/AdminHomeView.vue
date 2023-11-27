<template>
  <div class="title-bar">
    <h2>Admin Home Page</h2>
    <RouterLink to="/">Log out</RouterLink>
  </div>
  <main class="home">
    <div class="cards">

      <div class="card-row">
        <div class="card-title">
          <p>Manage Courses</p>
          <div class="course-actions">
            <button type="submit">Add Course</button>
            <p class="action-desc">To add a course, fill in all required boxes and click 'Add Course'.</p>
            <button type="submit">Edit Course</button>
            <p class="action-desc">To edit a course, fill in the course's name and additional changes. Then, click 'Edit Course'.</p>
            <button type="submit">Remove Course</button>
            <p class="action-desc">To remove a course, fill in the course's name and click 'Remove Course'.</p>
          </div>
        </div>
        <div class="actions">
          <form id="course-form" class="course-form">
            <input type="text" id="inputField" name="inputField" placeholder="Course Name">
            <input type="text" id="inputField" name="inputField" placeholder="Credits">
            <input type="text" id="inputField" name="inputField" placeholder="Course Title">
            <input type="text" id="inputField" name="inputField" placeholder="Start Time">
            <input type="text" id="inputField" name="inputField" placeholder="End Time">
            <input type="text" id="inputField" name="inputField" placeholder="Days">
            <input type="text" id="inputField" name="inputField" placeholder="Department">
            <input type="text" id="inputField" name="inputField" placeholder="Professor">
            <input type="text" id="inputField" name="inputField" placeholder="Max Enrollment">
            <input type="text" id="inputField" name="inputField" placeholder="Current Enrollment">
            <input type="text" id="inputField" name="inputField" placeholder="Prerequisites">
          </form>
        </div>
      </div>
 
      <div class="card-row">
        <div class="card-title">
          <p>Manage Students</p>
          <div class="course-actions">
            <button type="submit">Add Student</button>
            <p class="action-desc">To add a student, fill in all required boxes and click 'Add Student'.</p>
            <button type="submit">Edit Student</button>
            <p class="action-desc">To edit a course, fill in the student's id and additional changes. Then, click 'Edit Student'.</p>
            <button type="submit">Remove Student</button>
            <p class="action-desc">To remove a student, fill in the student's id and click 'Remove Student'.</p>
          </div>
        </div>
        <div class="actions">
          <form id="course-form" class="course-form">
            <input type="text" id="inputField" name="inputField" placeholder="ID">
            <input type="text" id="inputField" name="inputField" placeholder="Name">
            <input type="text" id="inputField" name="inputField" placeholder="Major">
            <input type="text" id="inputField" name="inputField" placeholder="Minor">
            <input type="text" id="inputField" name="inputField" placeholder="Standing">
            <input type="text" id="inputField" name="inputField" placeholder="GPA">
            <input type="text" id="inputField" name="inputField" placeholder="Total Credits">
            <input type="text" id="inputField" name="inputField" placeholder="Enrolled Credits">
            <input type="text" id="inputField" name="inputField" placeholder="Enrolled Courses">
            <input type="text" id="inputField" name="inputField" placeholder="Past Courses">
          </form>
        </div>
      </div>
 
      <div class="card-row">
        <div class="card-title">
          <p>Manage Professors</p>
          <div class="course-actions">
            <button type="submit">Add Professor</button>
            <p class="action-desc">To add a professor, fill in all required boxes and click 'Add Professor'.</p>
            <button type="submit">Edit Professor</button>
            <p class="action-desc">To edit a professor, fill in the professor's id and additional changes. Then, click 'Edit Professor'.</p>
            <button type="submit">Remove Professor</button>
            <p class="action-desc">To remove a professor, fill in the professor's id and click 'Remove Professor'.</p>
          </div>
        </div>
        <div class="actions">
          <form id="course-form" class="course-form">
            <input type="text" id="inputField" name="inputField" placeholder="ID">
            <input type="text" id="inputField" name="inputField" placeholder="Name">
            <input type="text" id="inputField" name="inputField" placeholder="Department">
            <input type="text" id="inputField" name="inputField" placeholder="Current Courses">
          </form>
        </div>
      </div>

    </div>
  </main>
 </template>


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
    background-color: #b3caf4;
    width: 25%;
    height: 28rem;
    border-radius: 0.4rem;
    margin: 1rem;
    padding: 0.8rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    font-size: 1.2rem;
    -webkit-text-fill-color: #f4f8ff;
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

  .course-form {
    width: 95%;
    height: 80%;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    row-gap: 4px;
    -webkit-text-fill-color: #8caff0;
  }

  .course-form input {
    height: 3rem;
  }

  .actions {
    background-color: #f4f8ff;
    width: 70%;
    height: 28rem;
    border-radius: 0.4rem;
    margin: 1rem;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    font-size: 1.2rem;
    -webkit-text-fill-color: #b3caf4;
  }

  button[type="submit"] {
    background: #f4f8ff;
    width: 12rem;
    height: 2rem;
    padding: 0.8rem;
    border-radius: 0.4rem;
    -webkit-text-fill-color: #b3caf4;
    font-size: 0.8rem;
    display: flex;
    align-items: center;
    justify-content: center;
  }
 
 
  </style>