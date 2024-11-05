<template>
    <div id='default'>
      <header class='header'>
        <div class='headline'>
          <div class="logo"><b>Library</b></div> 
          <!-- フォームのsubmitイベントがデフォルトではページをリロードしてしまいます。それを防ぐために、@submit.preventを使います。 -->
          <div class='search-div' v-if="isSuperUser">
            <form class="search-form"  @submit.prevent="search">
              <input  v-model="query" type="text" placeholder="本を検索..." class="search-input"/>
              <button type="submit" class="search-button">🔍</button>
            </form>
          </div>
          <div class='search-div' v-else>
            <form class="search-form" >
              <input  v-model="query" type="text" placeholder="本を検索..." class="search-input"/>
              <button type="submit" class="search-button">🔍</button>
            </form>
          </div>
          <nav class='nav'> 
            <ul class="head">
              <li class="home"><router-link to="/">Home</router-link></li>
              <li class="detail"><router-link to="/about/">About</router-link></li>
              <li class="profile">
                <router-link v-if="isAuthenticated" to="/profile">{{ user.username }}</router-link>
                <button v-else @click="handleLogout()">logout</button>
              </li>
              <!-- <li class="logout"><button @click="handleLogout()">logout</button></li> -->
            </ul>
          </nav>
        </div>
      </header>
      <main class='main'>
        <router-view />  
      </main>
      <footer class='footer'>
        <p class='p-line'>&copy; 2024 Libra </p>
      </footer>
    </div>
  </template>
  
<script>
  // import { CustomUserLogour } from '@/services/authService';

  // import axios from 'axios';

import { mapGetters } from "vuex";
export default {
  name: 'DefaultLayout',
  data() {
    return{
      error: '',
      query: '',
      books: [],
    };
  },
    computed: {
      ...mapGetters(['user', 'isAuthenticated']),
      isSuperUser() {
            console.log("User:", this.user);
            // console.log("Is SuperUser:", this.user.is_superuser);
            return this.user && this.user.is_superuser;
        },
    },
    created() {
        // if (!this.user) {
        //     // ページ表示時にユーザー情報がない場合は取得
        //     this.$store.dispatch('fetchUser');
        // }
        if (!this.user) {
            this.$store.dispatch('fetchUser').then(() => {
                if (!this.user) {
                    console.log("User information not loaded");
                }
            });
        }
    },
    methods: {
      async search() {
        if (this.query) {
          this.$router.push({ name: 'SearchResult', query: { q: this.query } });
        }else {
          alert('検索クエリを入力してください。');
        }
      },
      async handleLogout() {
            try {
                await this.$store.dispatch('logout');
                this.$router.push("/login");
            } catch (error) {
                console.error("Logout failed:", error);
            }
      },
    }
  };
</script>
  
<style>
/* Default Layout */
#default {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
header {
    background-color: #4a90e2;
    padding: 15px 30px;
    color: white;
  }
  
  .headline {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  /* ロゴのスタイル */
  .logo {
    font-size: 24px;
    font-weight: bold;
    letter-spacing: 2px;
  }
  input[type="text"].search-input{
    padding: 8px 12px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
    width: 500px;
    margin-left: 50px;
    transition: width 0.3s ease;
  }
  .search-button{
    background-color: #4a90e2;
    color: white;
    border: none;
    padding: 8px 12px;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .search-button:hover {
    background-color: #63a7f5;
  }
  /* ナビゲーションスタイル */
  /* nav ul {
    list-style: none;
    display: flex;
    gap: 15px;
  }
  
  nav ul li {
    display: inline;
  }
  
  nav a {
    color: white;
    text-decoration: none;
    font-weight: 500;
    font-size: 18px;
    transition: color 0.3s;
  }
  
  nav a:hover {
    color: #e0e0e0;
  }
   */
  /* メインコンテンツエリア */
  main {
    flex: 1;
    padding: 30px;
    margin: 20px;
    border-radius: 8px;
  }
  
  /* フッターのスタイル */
  footer {
    background-color: #4a90e2;
    color: white;
    text-align: center;
    padding: 10px 0;
    font-size: 14px;
  }
  
  /* レスポンシブ対応 */
  @media (max-width: 768px) {
    .headline {
      flex-direction: column;
      align-items: flex-start;
    }
  
    nav ul {
      flex-direction: column;
      gap: 10px;
    }
  
    main {
      margin: 10px;
    }
  }
</style>
  