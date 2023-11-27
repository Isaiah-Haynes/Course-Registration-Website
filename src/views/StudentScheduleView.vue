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
    <main class="home">
      <h2>Student Schedule View</h2>
      <p>
        This is the student schedule view.
      </p>
    </main>
  </template>
  
  <style>
  .home {
    padding: 1rem;
  }
  
  .home h2 {
    font-size: 1.75rem;
    margin-bottom: .75rem;
	text-align: center;
	font-weight: bold;
  }
  
  .home h3 {
    font-size: 1rem;
    margin-bottom: 1.5rem;
	text-align: center;
  }
  
  .home p {
    margin-bottom: 1rem;
	text-align: center;
  }
  </style>
  