import {createRouter, createWebHistory} from "vue-router";
import UserLogin from '@/components/views/Login.vue';
import UserRegister from '@/components/views/Register.vue';
import HomeIndex from "@/components/views/Index.vue";
import AccountProfile from "@/components/views/Account.vue";
import AuthLayout from "@/components/layout/AuthLayout.vue";
// import UserLogout from "@/components/views/Logout.vue";
import DefaultLayout from "@/components/layout/DefaultLayout.vue";
import SearchResult from "@/components/views/SearchResult.vue";
import fetchBookDetail from "@/components/views/BooksDetails.vue";
const routes = [
    {
        path: '/',
        component: DefaultLayout, // デフォルトページ専用のレイアウト
        children: [
            {path: "", name: 'Index', component: HomeIndex},
            {path: "profile/:name", name: "account", component: AccountProfile, props: true},
            { path: 'search', name: "SearchResult", component: SearchResult, props: (route) => ({ query: route.query.q })},
            {path: 'books/:id', name: "fetchBookDetail", component: fetchBookDetail, props: true},
        ],
      },
    {
        path: '/accounts',
        component: AuthLayout, // ログイン専用レイアウト
        children: [
            { path: '/:pathMatch(.*)*', redirect: '/accounts/login'},
            { path: '', redirect: '/accounts/login',},
            { path: 'login', name: 'Login', component: UserLogin },
            { path: 'register', name: 'Register', component: UserRegister},
            // { path: "logout", name: "Logout", component: HomeIndex},
        ],
      },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router