import {createRouter, createWebHistory} from "vue-router";
import UserLogin from '../views/Login.vue';
import UserRegister from '../views/Register.vue';
import HomeIndex from "../views/Index.vue";
import AccountProfile from "../views/Account.vue";
import AuthLayout from "../layout/AuthLayout.vue";
import DefaultLayout from "../layout/DefaultLayout.vue";
const routes = [
    // {path: "/accounts/login", name: 'Login', component: UserLogin},
    // {path: "/accounts/register", name: 'register', component: UserRegister},
    // {path: "/", name: 'Index', component: HomeIndex},
    // {path: "/profile", name: "account", component: AccountProfile},
    {
        path: '/',
        component: DefaultLayout, // ログイン専用レイアウト
        children: [
            {path: "/", name: 'Index', component: HomeIndex},
            {path: "/profile", name: "account", component: AccountProfile},
        ],
      },
    {
        path: '/accounts',
        component: AuthLayout, // ログイン専用レイアウト
        children: [
          { path: '/login', name: 'Login', component: UserLogin },
          { path: '/register', name: 'Register', component: UserRegister}
        ],
      },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router