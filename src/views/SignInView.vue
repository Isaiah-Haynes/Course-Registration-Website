<template>
  <div id="SignIn">
    <main class="form">
      <div class="pageTitle">
        <h2>Welcome Back!</h2>
        <h3>Sign In</h3>
      </div>

      <!-- Sign-in form below -->
      <!-- <form @submit.prevent="loginWithPassword"> -->
      <form class="signInBox">
        <div class="email">
          <input type="text" placeholder="email or username" />
        </div>
        <div class="password">
          <input type="password" placeholder="password" />
        </div>
        <div class="loginButtons">
          <p><button class="lButton" type="submit" >Student Login</button></p>  
          <p><button class="lButton" type="submit" >Professor Login</button></p>
          <p><button class="lButton" type="submit" >Administrator Login</button></p>
        </div>
      </form>

    </main>
  </div>
</template>

<style>
  #SignIn {
    min-height: 100vh;
    background-color: #8EC5FC;
    background-image: linear-gradient(62deg, #8EC5FC 0%, #E0C3FC 100%);
    display: flex;
    justify-content: center;
  }

  .pageTitle {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0.8rem;
  }

  .form {
    padding: 1rem;
    height: 36rem;
    width: 28rem;
    display: flex;
    flex-direction: column;
    background: #fefeff;
    border: none;
    box-shadow: 0px 0px 12px 0.8px #8682ce;
    margin: 75px;
    border-radius: 1rem;
  }
  
  .form h2 {
    font-size: 1.5rem;
    margin-bottom: 2rem;
  }
  
  .form p {
    margin-bottom: .5rem;
  }
  
  /* flex layouts allow us to position elements next to each other that would otherwise have been on top of each other */
  .form ul {
    display: flex;
    gap: 1rem;
    flex-direction: column;
  }
  .form li {
    display: flex;
    gap: 0.5rem;
    align-items: center;
  }
  
  /* create some space beneath the create todo form */
  .form form {
    margin-bottom: 1rem;
  }

  .email {
    display: flex;
    justify-content: center;
    margin: 1.2rem 1.2rem 0.6rem 1.2rem;
  }
  
  .password {
    display: flex;
    justify-content: center;
    margin: 0.6rem 1.2rem 1.2rem 1.2rem;
  }

  .loginButtons {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center; 
  }

  .lButton{
    margin: 0.4px;
    width: 12rem;
    background-color: #fefeff;
    -webkit-text-fill-color: #8eb1fc;
  }

  .lButton:hover {
    background-color: #8eb1fc;
    -webkit-text-fill-color: #fefeff;
  }

  .signInBox {
    display: flex;
    flex-direction: column;
    align-content: center;
  }
  
  /* set some default styling to buttons and inputs for borders, heights, and padding */
  .form :is(input, button) {
    line-height: 2rem;
    padding-inline: 0.5rem;
    border-radius: 0.375rem;
    border: 1px solid #ececec;
    margin-left: 0.5rem;
    color: #202020;
  }
</style>
