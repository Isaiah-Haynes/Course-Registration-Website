<template>
    <button class="button__login" @click="handleLogin">Administrators</button>
  </template>
  
  <script setup>
  import { useAuth0 } from "@auth0/auth0-vue";
  
  const { loginWithRedirect } = useAuth0();
// const loginWithRedirect = useAuth0();
  
  const handleLogin = () => {
    loginWithRedirect({
      appState: {
        target: "/admin/home",
      },
    });
  };
  </script>