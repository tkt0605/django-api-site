import {createRouter, createWebHistory} from "vue-router";
import Login from '@/components/Login.vue';
import Register from '@/components/Register.vue';
import Index from "@/components/Index.vue";

const routes = [
    {path: "/", name: 'Index', components: Index},
    {path: "/accounts/login", name: 'Login', components: Login},
    {path: "/accounts/register", name: 'register', components: Register},
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router