<template>
  <div>
    <h2>API Message</h2>
    <p v-if="message">{{message}}</p>   
  </div>
</template>
  
<script>
import axios from 'axios';

export default {
  // name: 'ルーター名'を入れないと、index.jsでのrouterを取得できませんでした。
  name: "HomeIndex",
  data() {
    return {
      message: '',  // messageを初期化して定義
    };
  },
  methods: {
    async index() {
      try {
        //認証トークンがあるかの確認のコード
        const token = localStorage.getItem('token');
        if (!token) {
          console.error("トークンが見つかりません。");
          this.message = '認証トークンが見つかりません。ログインしてください。'
          return
        }

        const response = await axios.get('http://localhost:8000/api/hello/', {
          headers: {
            //　トークンの自動送信で認証トークンの有無を調べる。
            Authorization: `Bearer ${token}`,

          },
        });
        console.log(response.data);
        this.message = response.data.message;
      } catch (error) {
        console.error(error.response ? error.response.message: error.message);
        this.message='APIの読み出しに失敗しました。';
      }
    },
  },
  mounted() {
    this.index()
  },
};
</script>
  