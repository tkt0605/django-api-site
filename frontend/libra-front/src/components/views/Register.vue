<template>
  <div>
      <h2>登録</h2>
      <form @submit.prevent="handleRegister">
          <input v-model="email" class='email' type="email" placeholder="メールアドレス" required />
          <input v-model="username" class="username" type="text" placeholder="ユーザー名" required />
          <input v-model="password1" class="password" type="password" placeholder="パスワード" required />
          <input v-model="password2" class="password2" type="password" placeholder="パスワード確認" required />
          <button type="submit">登録</button>
          <p>アカウントをお持ちであれば<router-link>ログイン</router-link>してください。</p>
      </form>
  </div>
</template>

<script>
// import { useStore } from 'vuex';

export default {
  name: 'UserRegister',
  data() {
      return {
          email: '',
          username: '',
          password1: '',
          password2: ''
      };
  },
  methods: {
      async handleRegister() {
          try {
              await this.$store.dispatch('register', {
                  email: this.email,
                  username: this.username,
                  password1: this.password1,
                  password2: this.password2
              });
              this.$router.push('/login');
          } catch (error) {
              console.error("Registration failed:", error);
          }
      }
  }
};
</script>
