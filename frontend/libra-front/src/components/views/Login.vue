<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
      <input class='email' v-model="email" placeholder="Email" type="email" />
      <input class='password' v-model="password" placeholder="Password" type="password" />
      <button type="submit">Login</button>
      <p>アカウントをお持ちでは無ければ<router-link>サインアップ</router-link>してください。</p>
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
  computed: {
    ...mapActions(['login']),
  },
  methods: {
    async handleLogin() {
    try {
      // ログインを試みる
      const response = await this.$store.dispatch('login', {
        email: this.email,
        password: this.password
      });

      // ログインが成功した場合にリダイレクト
      if (response && response.access) {
        this.$router.push('/');  // ログイン後のリダイレクト先
      } else {
        this.errorMessage = "Failed to login. Please check your credentials.";
      }
    } catch (error) {
      console.error("Failed to login:", error);
      this.errorMessage = "Failed to login. Please check your credentials.";
    }
  }
  },
};
</script>
