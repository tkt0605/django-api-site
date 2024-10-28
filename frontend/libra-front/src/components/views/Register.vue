<template>
    <div id="register-form">
      <h2>Register</h2>
      <form @submit.prevent="register" class="form" method="POST">
        <input class="form-input" type="text" v-model="email" placeholder="Email" required />
        <input class="form-input" type="text" v-model="username" placeholder="UserName" required/>
        <input class="form-input" type="password" v-model="password1" placeholder="Password" required />
        <input class="form-input" type="password" v-model="password2" placeholder="Confirm Password" required />
        <button class="submit-button" type="submit">Register</button>
      </form>
      <div class="other-page">
        <p>アカウントをお持ちの場合。<router-link to="/accounts/login">ログイン</router-link></p>
        <p v-if="errorMessage">{{ errorMessage }}</p>
      </div>
    </div>
  </template>
  
  <script>
import { register } from '@/services/authService';

// import router from '@/router';
// import axios from 'axios';
export default {
  name: 'UserRegister',  // 名前を変更
  data() {
    return {
      email: '',
      username: '',
      password1: '',
      password2: '',
      errorMessage: ''
    };
  },
  methods: {
    async register() {
      try {
        const response = await register(this.email, this.username, this.password1, this.password2);
        console.log('Register Success: ', response);
        if (response.key) {
          localStorage.setItem('authToken', response.key);
          console.log("Token saved:", localStorage.getItem('authToken', response.key))
          this.$router.push('login/');
        } else{
          throw new Error("登録できませんでした。");
        }
      }catch(error){
        console.error("Login Error: ", error.response || error.message);
        throw error
      }
    }
  }
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
  