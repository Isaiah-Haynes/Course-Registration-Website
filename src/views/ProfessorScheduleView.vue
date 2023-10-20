<template>
  <nav>
    <ul class="nav-links">
      <li>
        <RouterLink to="/professor/home">Home</RouterLink>
      </li>
      <li>
        <RouterLink to="/">Log out</RouterLink>
      </li>
    </ul>
  </nav>
    <main class="home">
      <h2>Professor Schedule View</h2>
      <p>
        This is the professor schedule view page.
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
  