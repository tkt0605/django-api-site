<template>
    <div id='app'>
      <header>
        <div class='headline'>
          <div class="logo"><b>Libra</b></div> 
          <form class="search-form">
            <input  v-model="query" @keyup.enter="search" type="text" placeholder="本を検索..." class="search-input"/>
            <button @click="SearchBooks" type="submit" class="search-button">🔍</button>
          </form>
          <nav> 
            <ul class="head">
              <li class="home"><router-link to="/">Home</router-link></li>
              <li class="detail"><router-link to="/about/">About</router-link></li>
              <li class="profile"><router-link to="/profile">MyName</router-link></li>
            </ul>
          </nav>
        </div>
      </header>
      <main>
        <div class="seach_result">
          <ul>
            <li v-for="book in books" :key="book.id">
              <strong>{{ book.volumeInfo.title }}</strong> by<em>{{ book.volumeInfo.authors?.join(', ') }}</em>
            </li> 
          </ul>
        </div>
        <router-view />  
      </main>
      <footer>
        <p>&copy; 2024 Libra </p>
      </footer>
    </div>
  </template>
  
  <script>
  export default {
    name: 'DefaultLayout',
    data() {
      return{
        error: '',
        query: '',
      };
    },
    methods: {
      async search() {
        if (this.query) {
        // 検索結果ページに検索クエリを渡して遷移
        this.$router.push({ name: 'SearchResults', query: { q: this.query } });
      }
    },
  },
  }
  </script>
  
  <style>
  /* リセットCSS */
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Arial', sans-serif;
  }
  
  /* ページ全体の背景 */
  body {
    background-color: #f5f5f5;
    color: #333;
    line-height: 1.6;
  }
  
  /* アプリ全体のスタイル */
  #app {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }
  
  /* ヘッダーのデザイン */
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
  .search-input{
    padding: 8px 12px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
    width: 200px;
    margin-left: 100px;
    transition: width 0.3s ease;
  }
  .search-input:focus {
    width: 500px;
    border-color: #4a90e2;
    outline: none;
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
  nav ul {
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
  