<template>
  <div>
    <h2>API Message</h2>
    <p v-if="message">{{message}}</p>   
  </div>
</template>
  
<script>
import axios from 'axios';
import { HelloWorld } from '@/services/authService';
export default {
  // name: 'ルーター名'を入れないと、index.jsでのrouterを取得できませんでした。
  name: "HomeIndex",
  data() {
    return {
      message: '',  // messageを初期化して定義
    };
  },
  methods: {
    async fetchMessage() {
      try{
        const data = await HelloWorld();
        this.message = data.message;
      } catch(error){
        console.log("メッセージの取得に失敗しました。", error);
      }
    },
  },
};
</script>
  