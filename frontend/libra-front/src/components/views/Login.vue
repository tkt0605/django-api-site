
<template>
  <div id="login-form">
    <h2>Login</h2>

    <form @submit.prevent="login" method='POST'>
      <input type="text" v-model="email" placeholder="Email" required />
      <input type="password" v-model="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
    <div class="'other-page'">
      <p>アカウントをお持ちでない場合<RouterLink to="/accounts/register">サインアップ</RouterLink></p>
      <p v-if="errorMessage">{{ errorMessage }}</p>
    </div>
  </div>
</template>

<script>
// import axios from 'axios';
import {login} from '@/services/authService'
export default {
  name: 'UserLogin',  // 名前を変更
  data() {
    return {
      email: '',
      password: '',
      errorMessage: '',
    };
  },
  methods: {
    async login() {
      // try {
      //   const response = await axios.post("http://localhost:8000/api/auth/login/", {
      //     username: this.email,
      //     password: this.password,
      //   });
      //   localStorage.setItem('token', response.data.access);
      //   localStorage.setItem('refresh_token', response.data.refresh)
      //   this.$router.push("/"); 
      // } catch(error) {
      //   console.error(error);
      //   alert('ログインに失敗しました。');
      // }
      try {
        const response = await login(this.email, this.password);
        console.log("Login Success:", response);
        localStorage.setItem('token', response.data.access);
        localStorage.setItem('refresh_token', response.data.refresh);
        this.$router.push('/');
      } catch(error) {
        console.error(error);
        this.errorMessage = 'ログインに失敗しました。';
      }
    },
  },
};
</script>
<style>
#login-form{
  text-align: center;
}
</style>