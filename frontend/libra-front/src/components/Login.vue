<template>
    <div>
      <h1>ログイン</h1>
      <form @submit.prevent="login">
        <input type="email" v-model="email" placeholder="Eメール" required />
        <input type="password" v-model="password" placeholder="パスワード" required />
        <button type="submit">ログイン</button>
      </form>
      <p v-if="message">{{ message }}</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        email: '',
        password: '',
        message: ''
      };
    },
    methods: {
      async login() {
        try {
          const response = await fetch('http://localhost:8000/api/auth/login/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              email: this.email,
              password: this.password
            })
          });
  
          if (response.ok) {
            const data = await response.json();
            this.message = 'ログイン成功！ トークン: ' + data.access;
            localStorage.setItem('token', data.access);  // トークンを保存
          } else {
            const errorData = await response.json();
            this.message = 'エラー: ' + JSON.stringify(errorData);
          }
        } catch (error) {
          console.error('ログインエラー:', error);
          this.message = 'ログインに失敗しました。';
        }
      }
    }
  };
  </script>
  