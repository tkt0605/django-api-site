// import Vue from 'vue'
import { createApp } from 'vue';  // Vue 3用のインポート
import router from './router';  // ルーターをインポート
import App from './App.vue';
import axios from 'axios';
import store from "./store"
const app = createApp(App);  // Vueインスタンスを作る・ここがないとテンプレート表示出来ないので注意
// token(dajngorestframework-simpleのJWT)を読み込みを自動化するためのコード
axios.interceptors.request.use((config) =>{
    const token = localStorage.getItem('token');
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});
app.use(router);
app.use(store)
app.mount('#app');
