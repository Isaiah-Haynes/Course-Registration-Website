<template>
  <div class="title-bar">
    <h2>Admin Home Page</h2>
    <RouterLink to="/">Log out</RouterLink>
  </div>
  <main class="home">
    <div class="cards">
 
      <div class="card-row">
        <p class="card-title">Manage Students</p>
        <div class="actions">
          <p>Add Student</p>
          <p>Edit Student</p>
          <p>Remove Student</p>
        </div>
      </div>
 
      <div class="card-row">
        <p class="card-title">Manage Professors</p>
        <div class="actions">
          <p>Add Professor</p>
          <p>Edit Professor</p>
          <p>Remove Professor</p>
        </div>
      </div>

      <div class="card-row">
        <p class="card-title">Manage Courses</p>
        <div class="actions">
          <p>Add Course</p>
          <p>Edit Course</p>
          <p>Remove Course</p>
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
    background-color: white;
    display: flex;
  }
 
 
  .card-title {
    background-color: #b3caf4;
    width: 16%;
    height: 12rem;
    border-radius: 0.4rem;
    margin: 1rem;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 1.2rem;
    -webkit-text-fill-color: #f4f8ff;
  }
 
 
  .actions {
    background-color: #f4f8ff;
    width: 82%;
    height: 12rem;
    border-radius: 0.4rem;
    margin: 1rem;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 1.2rem;
    -webkit-text-fill-color: #b3caf4;
  }
 
 
  </style>