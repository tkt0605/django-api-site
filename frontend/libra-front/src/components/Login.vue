
<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input type="text" v-model="email" placeholder="Email" required />
      <input type="password" v-model="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'UserLogin',  // 名前を変更
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    async login() {
      console.log('Login attempt:', this.email);
    },
  },
};
</script>
