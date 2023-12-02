<template>
  <div id="SignIn">
    <main class="form">
      <div class="pageTitle">
        <h2>Welcome Back!</h2>
        <h3>Sign In</h3>
      </div>
      <form class="signInBox">
        <div class="email">
          <input type="text" placeholder="User ID" />
        </div>
        <div class="password">
          <input type="password" placeholder="Password" />
        </div>
        <div class="loginButtons">
          <router-link to="/student/schedule">
            <button class="lButton" type="submit" >Student Login</button>
          </router-link>
          <router-link to="/professor/schedule">
            <button class="lButton" type="submit" >Professor Login</button>
          </router-link>
          <router-link to="/admin/home">
            <button class="lButton" type="submit" >Administrator Login</button>
          </router-link>
        </div>
      </form>

    </main>
  </div>
</template>
<style>
  #SignIn {
    overflow: hidden;
    height: 92vh;
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
    align-items: center;
    background: #fefeff;
    border: none;
    box-shadow: 0px 0px 12px 0.8px #8682ce;
    border-radius: 1rem;
    margin: 2rem;
  }
  
  .form h2 {
    font-size: 1.5rem;
    margin-bottom: 2rem;
  }

  .email {
    display: flex;
    justify-content: center;
  }
  
  .password {
    display: flex;
    justify-content: center;
  }

  .loginButtons {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 2rem;
  }

  .lButton{
    margin: 0.4px;
    width: 12rem;
    background-color: #fefeff;
    -webkit-text-fill-color: #3e71dc;
    margin: 0.4rem 1rem 0.4rem 1rem;
  }

  .lButton:hover {
    background-color: #3e71dc;
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
