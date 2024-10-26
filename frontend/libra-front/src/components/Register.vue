<template>
    <div>
      <h2>Register</h2>
      <form @submit.prevent="register">
        <input type="text" v-model="email" placeholder="Email" required />
        <input type="text" v-model="username" placeholder="UserName" required/>
        <input type="password" v-model="password1" placeholder="Password" required />
        <input type="password" v-model="password2" placeholder="Confirm Password" required />
        <button type="submit">Register</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'UserRegister',  // 名前を変更
    data() {
      return {
        email: '',
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
  