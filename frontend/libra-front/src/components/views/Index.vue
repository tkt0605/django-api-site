<template>
  <div class="BookList">
    <ul>
      <li v-for="book in books" :key="book.id" class="list">
        <router-link :to="{name: 'fetchBookDetail', params: {id: book.id}}">
          <img
            :src="book.volumeInfo.imageLinks.thumbnail || book.volumeInfo.imageLinks.smallThumbnail" 
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
export default {
    name: 'HomeIndex',
    data() {
      return{
        error: '',
        // query: '',
        books: [],
      };
    },
    async created() {
      try{
        const response = await fetchBooks();
        this.books = response.data;
      }catch(error){
        console.error("書籍の一覧取得エラー:", error);
      }
    },
  };
</script>
  