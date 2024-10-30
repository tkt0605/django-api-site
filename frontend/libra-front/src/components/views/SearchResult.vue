<template>
    <div>
      <h1>Search Results for "{{ query }}"</h1>
      
      <div v-if="error" class="error">{{ error }}</div>
  
      <div v-if="books.length">
        <ul>
          <li v-for="book in books" :key="book.id">
            <strong>{{ book.volumeInfo.title }}</strong> by
            <em>{{ book.volumeInfo.authors?.join(', ') }}</em>
          </li>
        </ul>
      </div>
      <div v-else-if="!error">No books found for "{{ query }}".</div>
    </div>
  </template>
  
  <script>
  import { searchBooks } from '@/services/authService';
  
  export default {
    data() {
      return {
        books: [],  // 検索結果
        error: '',  // エラーメッセージ
      };
    },
    computed: {
      query() {
        return this.$route.query.q;  // URLのクエリパラメータから検索クエリを取得
      },
    },
    async created() {
      try {
        const data = await searchBooks(this.query);
        this.books = data.items || [];
      } catch (error) {
        this.error = '検索に失敗しました。もう一度お試しください。';
        console.error('Search Error:', error);
      }
    },
  };
  </script>
  
  <style>
  .error {
    color: red;
  }
  </style>
  