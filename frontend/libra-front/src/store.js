// store.js
import { createStore } from 'vuex';
import { register, login, logout, fetchUser } from '@/services/authService';
import axios from 'axios';

const store = createStore({
  state: {
    user: null,
    token: localStorage.getItem('token') || null,
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    setToken(state, token) {
      state.token = token;
      localStorage.setItem('token', token);
      axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    },
    clearAuthData(state) {
      state.token = null;
      state.user = null;
      localStorage.removeItem('token');
      localStorage.removeItem('refresh_token');
      delete axios.defaults.headers.common['Authorization'];
    },
  },
  actions: {
    async register({ commit }, { username, email, password1, password2 }) {
      try {
        const response = await register(username, email, password1, password2);
        commit('setUser', response.user); // 登録後にユーザー情報が返ってくる場合
        return response;
      } catch (error) {
        console.error("Registration error:", error);
        throw error;
      }
    },
    async login({ commit }, { email, password }) {
      try {
        const response = await login(email, password);
        if (response && response.access) {
          commit('setToken', response.access);
          commit('setUser', response.user); // ログイン後にユーザー情報が返ってくる場合
          return response;
        }
      } catch (error) {
        console.error("Login Error:", error);
        throw error;
      }
    },
    async logout({ commit }) {
      try {
        await logout();
        commit('clearAuthData');
      } catch (error) {
        console.error("Logout Error:", error);
        throw error;
      }
    },
    async fetchUser({ commit }) {
      try {
        const userData = await fetchUser();
        commit('setUser', userData);
        return userData;
      } catch (error) {
        console.error("Fetch User Error:", error);
        throw error;
      }
    },
  },
});

export default store;
