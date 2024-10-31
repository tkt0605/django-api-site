<template>
    <div>
      <div v-if="error" class="error">{{ error }}</div>
  
      <div v-if="books.length">
        <ul>
          <div>検索結果： "{{ query }}"</div>
          <li v-for="book in books" :key="book.id">
            <!-- <img :src="book.volumeInfo?.imageLinks?.thumbnail || 'https://via.placeholder.com/128x193?text=No+Cover'" alt="Book cover"class="book-cover"/> -->
            <strong>{{ book.volumeInfo.title }}</strong> by<em>{{ book.volumeInfo.authors?.join(', ') }}</em>
            <p>{{ book.volumeInfo.industryIdentifiers }}</p>
            <button @click='AddDatabaseBooks(book)'>AddBook</button>
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
        getCSRFToken(){
            const cookies = String(document.cookie).split(';');
            for (let cookie of cookies){
                const [name, value] = cookie.trim().split('=');
                if (name === "csrftoken") return decodeURIComponent(value)
            }
        return '';
        },
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
            try {
                if (!book || !book.volumeInfo){
                    alert('Invalid book data');
                    return;
                }
                console.log('book: ', book)
                // console.log('ISBN: ', book.volumeInfo?.industryIdentifiers);
                const csrftoken = this.getCSRFToken(); // 作成したcsrfTokenの取得
                const isbnData13 = book.volumeInfo.industryIdentifiers?.find((id)=> id.type==='ISBN_13') || {};
                const isbnData10 = book.volumeInfo.industryIdentifiers?.find((id)=> id.type==='ISBN_10') || {};
                const newBook ={
                    title: book.volumeInfo?.title,
                    publisher: book.volumeInfo?.publisher || '出版社',
                    publish_date: book.volumeInfo?.publishDate || '出版日',
                    author: book.volumeInfo?.author?.join(', ') || 'Unknown',
                    stock: 0,
                    price: 0,
                    isbn_10: isbnData10.identifier || '',
                    isbn_13: isbnData13.identifier || '',
                    language: book.volumeInfo?.language || "ja",
                };
                if (!isbnData13 && isbnData10){
                    console.log('この本には、ISBNは含まれていません.。');
                }
                // データをローカルデータベースに追加する時は、postを使用.
                // djangoで作成した本を追加するAPIであるBookAPIViewのリンクを張る。
                await axios.post('http://localhost:8000/api/book/', newBook, {
                    headers:{
                        "Content-Type": "application/json",
                        "X-CSRFToken": csrftoken,
                    },
                    withCredentials: true,
                });
                alert('Book added!');               
            } catch(error){
                console.error("AddDatabaseBooks Error:", error.response?.data || error.message);
                alert("Failed to add book.");
            }
        }
    },
};
</script>
  
  <style>
  .error {
    color: red;
  }
  </style>
  