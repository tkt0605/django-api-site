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
  mounted() {
    axios.get('http://localhost:8000/api/hello/')
      .then(response => {
        this.message = response.data.message;  // APIからのメッセージを代入
      })
      .catch(error => {
        console.error('APIエラー:', error);
      });
  },
};
</script>
  