import {createRouter, createWebHistory} from "vue-router";
import UserLogin from '@/components/Login.vue';
import UserRegister from '@/components/Register.vue';
import HomeIndex from "@/components/Index.vue";

const routes = [
    {path: "/", name: 'Index', component: HomeIndex},
    {path: "/accounts/login", name: 'Login', component: UserLogin},
    {path: "/accounts/register", name: 'register', component: UserRegister},
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router