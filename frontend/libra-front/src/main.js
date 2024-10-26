// import Vue from 'vue'
import { createApp } from 'vue';  // Vue 3用のインポート
import App from './App.vue';
import router from './router';  // ルーターをインポート

const app = createApp(App);  // Vueインスタンスを作
app.use(router);
app.mount('#app');
