<template>
    <div id="SignIn">
    <main class="form">
      <h2>Course Registration Sign in</h2>

      <!-- Sign-in form below -->
      <!-- <form @submit.prevent="loginWithPassword"> -->
        <form>
        <input type="text" placeholder="email or username" />
        <p>
            <input type="password" placeholder="password" />
        </p>
        <p>
            <button type="submit">Student Login</button>
        </p>  
        <p> 
            <button type="submit">Professor Login</button>
        </p>
        <button type="submit">Administrator Login</button>
      </form>

    </main>
    </div>
  </template>
  
  <style>
  #SignIn {
    min-height: 100vh;
    background-image: url("../images/StorrsAerial.jpeg");
  }
  .form {
    padding: 1rem;
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
  
  /* set some default styling to buttons and inputs for borders, heights, and padding */
  .form :is(input, button) {
    line-height: 2rem;
    padding-inline: 0.5rem;
    border-radius: 0.375rem;
    border: 1px solid #d9d9d9;
    margin-left: 0.5rem;
    color: #202020;
  }
  </style>
  