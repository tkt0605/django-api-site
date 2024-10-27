<template>
    <div id="register-form">
      <h2>Register</h2>
      <form @submit.prevent="register" class="form">
        <input class="form-input" type="text" v-model="email" placeholder="Email" required />
        <input class="form-input" type="text" v-model="username" placeholder="UserName" required/>
        <input class="form-input" type="password" v-model="password1" placeholder="Password" required />
        <input class="form-input" type="password" v-model="password2" placeholder="Confirm Password" required />
        <button class="submit-button" type="submit">Register</button>
      </form>
      <div class="other-page">
        <p>アカウントをお持ちの場合。<router-link to="/accounts/login">ログイン</router-link></p>
      </div>
    </div>
  </template>
  
  <script>
// import router from '@/router';

  export default {
    name: 'UserRegister',  // 名前を変更
    data() {
      return {
        email: '',
        username: '',
        password1: '',
        password2: '',
      };
    },
    methods: {
      async register() {
        console.log('Registration attempt:', this.email);
      },
    },
  };
  </script>

  <style>
  #register-form{
    text-align: center;
  }
  .form{
    display: block;
  }
  /* .input-form{

  } */
  </style>
  