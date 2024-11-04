<template>
  <div class="BookList">
    <div>
      <p v-if="isAuthenticated">Welcome, {{ user.username }}
        <!-- <router-link :to="{name: 'account', params:{name: user.username}}">{{ user.username }}</router-link> -->
      </p>
      <p v-else>ログインしていません。</p>
    </div>
    <ul>
      <li v-for="book in books" :key="book.id" class="list">
        <router-link :to="{name: 'fetchBookDetail', params: {id: book.id}}">
          <img 
                :src="book.image"
                alt="Book cover"
                class="book-cover"
                />
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
    return {
      error: '',
      books: [],
      isAuthenticated: false,
      user: null  // userを初期化
    };
  },
  async created() {
    try {
      const response = await fetchBooks();
      await this.checkAuthStatus();
      this.books = response.data;
    } catch (error) {
      console.error("書籍の一覧取得エラー:", error);
    }
  },
  methods: {
    async checkAuthStatus() {
      const token = localStorage.getItem('token');
      if (token) {
        try {
          const response = await axios.get('http://localhost:8000/api/accounts/profile/', {
            headers: {
              Authorization: `Bearer ${token}`
            }
          });
          this.user = response.data;  // user情報をセット
          this.isAuthenticated = true;
          console.log(this.user);
        } catch (error) {
          if (error.response && error.response.status === 401) {
            // トークンが無効な場合、リフレッシュを試みる
            const newToken = await this.refreshToken();
            if (newToken) {
              // 新しいトークンで再リクエスト
              await this.checkAuthStatus();
            } else {
              console.error("Authentication failed and refresh token expired:", error);
              this.isAuthenticated = false;
              this.user = null;
              // 必要であればログインページへリダイレクトする処理などを追加
            }
          } else {
            console.error("Authentication failed:", error);
            this.isAuthenticated = false;
            this.user = null;
          }
        }
      } else {
        this.isAuthenticated = false;
        this.user = null;
      }
    },
    async refreshToken() {
      const refreshToken = localStorage.getItem('refresh_token');
      if (refreshToken) {
        try {
          const response = await axios.post('http://localhost:8000/api/accounts/token/refresh/', {
            refresh: refreshToken
          });
          const newToken = response.data.access;
          localStorage.setItem('token', newToken);
          return newToken;
        } catch (error) {
          console.error("Token refresh failed:", error);
          return null;
        }
      }
      return null;
    },
    async login() {
      // ログイン処理
      await this.checkAuthStatus();
    },
    logout() {
      localStorage.removeItem('token');
      localStorage.removeItem('refresh_token');
      this.isAuthenticated = false;
      this.user = null;
    }
  }
};
</script>
<style>
.BookList {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.BookList p {
  font-size: 1rem;
  color: #555;
  margin: 10px 0;
}

.BookList p.isAuthenticated {
  font-weight: bold;
  color: #4CAF50;
}

.BookList p.notAuthenticated {
  color: #FF5252;
}

ul {
  list-style-type: none;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.list {
  width: 150px;
  text-align: center;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  overflow: hidden;
}

.list:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
}

.book-cover {
  width: 100%;
  height: auto;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}

.list p {
  font-size: 0.9rem;
  font-weight: bold;
  color: #333;
  margin: 10px 0;
}

router-link {
  text-decoration: none;
  color: inherit;
}

</style>