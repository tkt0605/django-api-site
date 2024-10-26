// import Vue from 'vue'
import { createApp } from 'vue';  // Vue 3用のインポート
import App from './App.vue';
import Account from './Account.Vue'
import router from './router';  // ルーターをインポート

const app = createApp(App);  // Vueインスタンスを作成
const account = createApp(Account)
app.use(router);
app.mount('#app');
account.use(router);
account.mount("#account")