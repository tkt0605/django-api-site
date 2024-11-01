<template>
  <div class="'BookList'">
    <ul v-for="book in books" :key="book.id">
      <li class="list">
        <router-link :to="{name: 'BooksDetails', params: {id: book.id}}">
          <p>{{ book.title }}</p>
        </router-link>
      </li>
    </ul>
  </div>
</template>
  
<script>
import { BooksList } from '@/services/apiService';
export default {
    name: 'HomeIndex',
    data() {
      return{
        error: '',
        // query: '',
        books: [],
      };
    },
    methods:{
      async created() {
        try{
          const response = await BooksList();
          this.books = response.data;
        }catch(error){
          console.error("書籍の一覧取得エラー:", error);
        }
      },
    },
  };
</script>
  