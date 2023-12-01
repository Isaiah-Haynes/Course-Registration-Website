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
  import { getProtectedResource } from "../util/api-setup";
import { ref } from "vue";
import { useAuth0 } from "@auth0/auth0-vue"; //STEP2

const message = ref("");

const getMessage = async () => {
  //const { data, error } = await getProtectedResource();
  const { getAccessTokenSilently } = useAuth0();  //STEP2
  const accessToken = await getAccessTokenSilently(); //STEP2
  const { data, error } = await getProtectedResource(accessToken); //STEP2

  if (data) {
    message.value = JSON.stringify(data, null, 2);
  }

  if (error) {
    message.value = JSON.stringify(error, null, 2);
  }
};

getMessage();
// console.log(message);
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
  