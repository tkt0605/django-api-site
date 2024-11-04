<template>
  <div class="BookList">
    <div>
      <p v-if="isAuthenticated">Welcome, {{ user.username }}</p>
      <p v-else>ログインしていません。</p>
    </div>
    <ul>
      <li v-for="book in books" :key="book.id" class="list">
        <router-link :to="{name: 'fetchBookDetail', params: {id: book.id}}">
          <!-- <img
            :src="book.volumeInfo.imageLinks.thumbnail || book.volumeInfo.imageLinks.smallThumbnail" 
            alt="Book cover"
            class="book-cover"
          /> -->
          <p>{{ book.title }}</p>
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import { fetchBooks } from '@/services/apiService';
import axios from 'axios';
export default {
    name: 'HomeIndex',
    data() {
      return{
        error: '',
        // query: '',
        books: [],
        isAuthenticated: false,
      };
    },
    async created() {
      try{
        const response = await fetchBooks();
        this.checkAuthStatus()
        this.books = response.data;
      }catch(error){
        console.error("書籍の一覧取得エラー:", error);
      }
    },
    methods: {
      async checkAuthStatus() {
        const token = localStorage.getItem('access_token')
        if (token) {
          try {
            const response = await axios.get('http://localhost:8000/api/accounts/profile/', {
              headers: {
                Authorization: `Bearer ${token}`
              }
            })
            this.user = response.data
            this.isAuthenticated = true
            console.log(this.user);
          } catch (error) {
            console.error("Authentication failed:", error)
            this.isAuthenticated = false
          }
        } else {
          this.isAuthenticated = false
        }
      },
      async login() {
        // ログイン処理
        this.checkAuthStatus()
      },
      logout() {
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        this.isAuthenticated = false
        this.user = null
      }
    }
};
</script>
  