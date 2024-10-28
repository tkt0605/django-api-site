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
      </div>
    </div>
  </template>
  
  <script>
// import router from '@/router';
import axios from 'axios';
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
      try {
        const response = await axios.post("http://localhost:8000/api/auth/registration/", {
          email: this.email,
          username: this.username,
          password1: this.password1,
          password2: this.password2,
        });
        localStorage.setItem('token', response.data.access);
        this.$router.push('/');
      } catch (error){
        console.error(error);
        alert('登録に失敗しました。');
      }
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
  