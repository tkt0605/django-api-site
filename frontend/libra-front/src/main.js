// import Vue from 'vue'
import { createApp } from 'vue';  // Vue 3用のインポート
import router from './router';  // ルーターをインポート
import App from './App.vue';

const app = createApp(App);  // Vueインスタンスを作る・ここがないとテンプレート表示出来ないので注意
app.use(router);
app.mount('#app');
