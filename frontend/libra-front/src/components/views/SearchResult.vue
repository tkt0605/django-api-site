<template>
    <div>
      <h1>Search Results for "{{ query }}"</h1>
      
      <div v-if="error" class="error">{{ error }}</div>
  
      <div v-if="books.length">
        <ul>
          <li v-for="book in books" :key="book.id">
            <!-- <img :src="book.volumeInfo?.imageLinks?.thumbnail || 'https://via.placeholder.com/128x193?text=No+Cover'" alt="Book cover"class="book-cover"/> -->
            <strong>{{ book.volumeInfo.title }}</strong> by<em>{{ book.volumeInfo.authors?.join(', ') }}</em>
            <button @click='AddDatabaseBooks()'>AddBook</button>
          </li>
        </ul>
      </div>
      <div v-else-if="!error">No books found for "{{ query }}".</div>
    </div>
  </template>
  
<script>
import { searchBooks } from '@/services/authService';
import axios from 'axios';

export default {
    props: ["query"],
    data() {
        return{
            books: [],
            error: '',
        }
    },
    watch:{
        query: {
            immediate: true,
            handler(newQuery) {
                this.perfomrsSearch(newQuery);
            },
        },
    },
    methods:{
        async perfomrsSearch(query) {
            if (!query) {
                this.error = "検索クエリが空です。";
                this.books = [];
                return;
            }
            try {
                const data = await searchBooks(query);
                console.log("APIからのデータ: ", data);
                if (data.items && data.items.length){
                    this.books =  data.items;
                    this.error = '';
                }else{
                    this.error = `「${query}」に一致する本が見つかりませんでした。`;
                    this.books = [];
                }
            }catch(error){
                this.error = "検索に失敗しました。";
                console.error("Search Error: ", error);
            }
        },
        async AddDatabaseBooks(book) {
            const isbnData = book.volumeInfo?.industryIdentifiers.find((id) => id.type === 'ISBN_13');
            const newBook ={
                title: book.volumeInfo?.title,
                publisher: book.volumeInfo?.publisher || '出版社',
                publish_date: book.volumeInfo?.publishDate || '出版日',
                authors: book.volumeInfo?.authors?.join(', ') || 'Unknown',
                stock: 0,
                price: 0,
                isbn_10: isbnData?.identifier || '',
                isbn_13: isbnData?.identifier || '',
                language: book.volumeInfo?.language || "ja",
            };
            // データをローカルデータベースに追加する時は、postを使用
            await axios.post('http://localhost:8000/api/books/', newBook);
            alert('Book added!');
        }
    },
};
</script>
  
  <style>
  .error {
    color: red;
  }
  </style>
  