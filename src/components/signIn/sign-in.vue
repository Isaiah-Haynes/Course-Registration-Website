<template>
    <div class="sign-in__container">
        <div class="sign-in__form">
            <div class="sign-in__pageTitle">
                <h2>Welcome Back!!</h2>
                <h3>Choose which site to log in to</h3>
            </div>
            <form class="sign-in__signInBox">
                <div class = sign-in__login-buttons>
                    <studentLogin />
                    <professorLogin />
                    <adminLogin />
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
import studentLogin from "@/components/buttons/student-login-button.vue";
import professorLogin from "@/components/buttons/professor-login-button.vue";
import adminLogin from "@/components/buttons/admin-login-button.vue";

</script>