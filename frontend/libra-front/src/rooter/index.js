import Vue from 'vue';
import Router from "vue-router";
import Login from '@/components/Login.vue';
import Register from '@/components/Register.vue';
import Index from "@/components/index.vue";

Vue.use(Router);
export default new Router({
    mode: "history",
    routes: [
        {path: "/", component: Index, name: 'index' },
        {path: "/accounts/login", component: Login, name: 'login'},
        {path: "/accounts/register", component: Register, name: "register"},
    ],
})