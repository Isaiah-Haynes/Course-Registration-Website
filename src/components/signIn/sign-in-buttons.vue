<template>
  <div class="sign-in__buttons">
    <template>
      <studentLoginButton />
      <professorLoginButton />
      <adminLoginButton />
    </template>
  </div>
</template>

<script setup>
import studentLoginButton from "@/components/buttons/student-login-button.vue";
import professorLoginButton from "@/components/buttons/professor-login-button.vue";
import adminLoginButton from "@/components/buttons/admin-login-button.vue";
</script>
