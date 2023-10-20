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
    <main class="home">
      <h2>Student Enroll View</h2>
      <p>
        This is the page for students to enroll in courses.
      </p>
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
  </style>
  