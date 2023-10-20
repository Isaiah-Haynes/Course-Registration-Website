<template>
  <nav>
    <ul class="nav-links">
      <li>
        <RouterLink to="/">Log out</RouterLink>
      </li>
    </ul>
  </nav>
    <main class="home">
      <h2>Admin Home Page</h2>
      <p>
        This is the admin home page, I assume most, if not all, admin related things can be accomplished
        from this one page
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
  