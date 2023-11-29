<template>
    <div class="sign-in__container">
        <div class="sign-in__pageTitle">
            <h2>Welcome Back!</h2>
            <h3>Choose which site to log in to below</h3>
        </div>
        <form class="sign-in__signInBox">
            <LoginButtons />
        </form>
    </div>
</template>

<script setup>
import LoginButtons from "@/components/signIn/sign-in-buttons.vue";
</script>