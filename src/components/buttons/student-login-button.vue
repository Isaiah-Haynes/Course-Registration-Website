<template>
    <button class="button__login" @click="handleLogin">Students</button>
</template>
  
  <script setup>
  import { useAuth0 } from "@auth0/auth0-vue";
  
  const { loginWithRedirect } = useAuth0();
  // const loginWithRedirect = useAuth0();
  
  const handleLogin = () => {
    loginWithRedirect({
      appState: {
        target: "/student/schedule",
      },
    });
  };
  </script>

<!-- <style>
  .button__login{
    margin: 0.4px;
    width: 12rem;
    background-color: #fefeff;
    -webkit-text-fill-color: #8eb1fc;
    margin: 0.4rem 1rem 0.4rem 1rem;
  }

  .button__login:hover {
    background-color: #8eb1fc;
    -webkit-text-fill-color: #fefeff;
  }

</style> -->