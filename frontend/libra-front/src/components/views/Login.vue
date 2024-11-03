<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
      <input v-model="email" placeholder="Email" type="email" />
      <input v-model="password" placeholder="Password" type="password" />
      <button type="submit">Login</button>
    </form>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: "UserLogin",
  data() {
    return {
      email: '',
      password: '',
      errorMessage: '',
    };
  },
  methods: {
    ...mapActions(['login']),
    async handleLogin() {
      try {
        await this.login({ email: this.email, password: this.password });
        this.$router.push('/'); // ログイン後にホームページへリダイレクト
      } catch (error) {
        this.errorMessage = 'Failed to login. Please check your credentials.';
      }
    },
  },
};
</script>
