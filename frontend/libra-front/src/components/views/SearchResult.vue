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
  props: ['query'], // クエリをpropsとして受け取る
  data() {
    return {
      books: [], // 検索結果
      error: '', // エラーメッセージ
    };
  },
  async created() {
    if (!this.query) {
      this.error = '検索クエリが空です。';
      return;
    }

    try {
      const data = await searchBooks(this.query);
      this.books = data.items || [];
      if (!this.books.length) {
        this.error = `「${this.query}」に一致する本が見つかりませんでした。`;
      }
    } catch (error) {
      this.error = '検索に失敗しました。';
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
  