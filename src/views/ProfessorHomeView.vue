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
  <main class="home">
    <h2>Professor Home Page</h2>
    <p>
      This is the professor home page.
    </p>
  </main>
</template>
<script setup>
import LogOut from "@/components/buttons/logout-button.vue";

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
</style>
  