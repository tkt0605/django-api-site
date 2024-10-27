
<template>
  <div id="login-form">
    <h2>Login</h2>

    <form @submit.prevent="login">
      <input type="text" v-model="email" placeholder="Email" required />
      <input type="password" v-model="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
    <div class="'other-page'">
      <p>アカウントをお持ちでない場合<RouterLink to="/accounts/register">サインアップ</RouterLink></p>
    </div>
  </div>
</template>

<script>
// import axios from 'axios';
export default {
  name: 'UserLogin',  // 名前を変更
  data() {
    return {
      email: '',
      password: '',
      message: '',
    };
  },
  methods: {
    async login(){
      try{
        const response = await fetch('http://localhost:8000/auth/login', {
          method: 'POST',
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({
            email: this.email,
            password:this.password,
          })
        });
        if (response.ok){
          const data = await response.json();
          this.message == 'ログイン成功! トークン: '+data.access;
          localStorage.setItem('token', data.access);
        }else{
          const errorData  = await response.json();
          this.message == 'エラー: '+ JSON.stringify(errorData);
        }
      } catch (error){
        console.log("ログインエラー: ", error);
        this.message == "ログインに失敗しました。";
      }
    }
  },
  // mounted() {
  //   axios POST('http')
  // }
};
</script>
<style>
#login-form{
  text-align: center;
}
</style>