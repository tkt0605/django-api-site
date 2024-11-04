<template>
    <div>
      <div v-if="error" class="error">{{ error }}</div>
  
      <div v-if="books.length">
        <ul>
          <div>検索結果： "{{ query }}"</div>
          <li v-for="book in books" :key="book.id">
            <router-link :to="{name: 'fetchBookDetail', params:{id: book.id}}">
                <img 
                :src="book.volumeInfo?.imageLinks?.thumbnail || book.volumeInfo?.imageLinks?.smallThumbnail" 
                alt="Book cover"
                class="book-cover"
                />
                <strong>{{ book.volumeInfo.title }}</strong> by<em>{{ book.volumeInfo.authors?.join(', ') }}</em>
            </router-link>
            <div v-if="isSuperUser">
                <div class="stock-container">
                    <label for="stock">在庫数:</label>
                    <input type="number" v-model="book.stock" min="0" class="stock-input" placeholder="在庫数" />
                </div>
                <button v-if="book.is_added" class="always-btn">alwaysAdd</button>
                <button v-else @click='AddDatabaseBooks(book)'>AddBook</button>
            </div>
          </li>
        </ul>
      </div>
      <div v-else-if="!error">No books found for "{{ query }}".</div>
    </div>
  </template>
  
<script>
import { searchBooks } from '@/services/authService';
import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
    props: ["query"],
    data() {
        return{
            books: [],
            error: '',
            isAuthenticated: false,
            user: null  // userを初期化
        }
    },
    computed: {
        ...mapGetters(['user', 'isAuthenticated']),
        isSuperUser() {
            return this.user && this.user.is_superuser;
        }
    },
    created() {
        if (!this.user) {
            // ページ表示時にユーザー情報がない場合は取得
            this.$store.dispatch('fetchUser');
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
        formatDateYMD(dataString){
            const date = new Date(dataString);
            const year = date.getFullYear();
            const month = String(date.getMonth() + 1).padStart(2, '0');
            const day = String(date.getDay()).padStart(2, '0');
            return `${year}-${month}-${day}`
        },
        async checkIfBookAdded(book) {
            // ここでAPIから既に追加されているか確認する処理を行います。
            // 例えば、ISBNでデータベースに問い合わせて存在確認する。
            try {
                const response = await axios.get(`http://localhost:8000/api/check_book/${book.isbn_13}`);
                return response.data.is_added; // 例えば `true` または `false` が返るとします
            } catch (error) {
                console.error("Error checking book:", error);
                return false;
            }
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
                // const csrftoken = this.getCSRFToken(); // 作成したcsrfTokenの取得
                const isbnData13 = book.volumeInfo.industryIdentifiers?.find((id)=> id.type==='ISBN_13') || {};
                const isbnData10 = book.volumeInfo.industryIdentifiers?.find((id)=> id.type==='ISBN_10') || {};
                const formatDateYMD = book.volumeInfo.publishedDate ? this.formatDateYMD(book.volumeInfo.publishedDate) : '1990-10-20';
                // const image_file = book.volumeInfo?.imageLinks.thumbnail || null;
                const newBook ={
                    title: book.volumeInfo?.title,
                    image: book.volumeInfo?.imageLinks?.thumbnail || null,
                    publisher: book.volumeInfo?.publisher || '出版社',
                    publish_date: formatDateYMD || '出版日',
                    author: book.volumeInfo?.authors?.join(', ') || 'Unknown',
                    stock: book.stock,
                    price: book.volumeInfo.price || 0, 
                    isbn_10: isbnData10.identifier || '',
                    isbn_13: isbnData13.identifier || '',
                    language: book.volumeInfo?.language || "ja",
                };
                if (!isbnData13 && isbnData10){
                    console.log('この本には、ISBNは含まれていません.。');
                }
                await axios.post('http://localhost:8000/api/book/', newBook, {
                    headers:{
                        "Content-Type": 'multipart/form-data',
                        // "X-CSRFToken": csrftoken,
                    },
                    // withCredentials: true,
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
  