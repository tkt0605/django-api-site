import {createRouter, createWebHistory} from "vue-router";
import UserLogin from '@/components/Login.vue';
import UserRegister from '@/components/Register.vue';
import HomeIndex from "@/components/Index.vue";

const routes = [
    {path: "/", name: 'Index', components: HomeIndex},
    {path: "/accounts/login", name: 'Login', components: UserLogin},
    {path: "/accounts/register", name: 'register', components: UserRegister},
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router