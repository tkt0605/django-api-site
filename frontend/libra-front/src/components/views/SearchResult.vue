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
                <div v-if="!book.is_added">
                    <div class="stock-container">
                        <label for="stock">在庫数:</label>
                        <input type="number" v-model="book.stock" min="0" class="stock-input" placeholder="在庫数" />
                    </div>
                    <button class="add_button" @click='AddDatabaseBooks(book)'>AddBook</button>
                </div>
                <button v-else class="always-btn">alwaysAdd</button>
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
        }
    },
    computed: {
        ...mapGetters(['user', 'isAuthenticated']),
        isSuperUser() {
            console.log("User object:", this.user);
            // console.log("Is SuperUser:", this.user ? this.user.is_superuser : 'No user data');
            return this.user && this.user.is_superuser;
        },
    },
    created() {

        if (!this.user) {
            this.$store.dispatch('fetchUser').then(() => {
                if (!this.user) {
                    console.log("User information not loaded");
                }
            });
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
            try {
                const isbn = book.isbn_13 || book.isbn_10;
                if (!isbn) {
                    console.error("No ISBN available in book data");
                    return false;
                }
                console.log(isbn);
                // const response = await axios.get('http://localhost:8000/api/check_book/', {is_added: book});
                const response = await axios.get(`http://localhost:8000/api/check_book/${isbn}/`);
                console.log("API response for is_added:", response.data.is_added);
                return response.data.is_added;
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
                    this.books = data.items;
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
                const isbnData13 = book.volumeInfo.industryIdentifiers?.find((id)=> id.type==='ISBN_13') || {};
                const isbnData10 = book.volumeInfo.industryIdentifiers?.find((id)=> id.type==='ISBN_10') || {};
                const formatDateYMD = book.volumeInfo.publishedDate ? this.formatDateYMD(book.volumeInfo.publishedDate) : '1990-10-20';
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

                    },

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
/* General Styling */
/* Error Message */
.error {
  color: #d9534f;
  background-color: #f2dede;
  padding: 10px;
  border: 1px solid #ebccd1;
  border-radius: 5px;
  margin-bottom: 15px;
  text-align: center;
}

/* Search Result Text */
div > div:first-child {
  font-size: 1.2em;
  font-weight: bold;
  margin-bottom: 20px;
  color: #333;
}

/* Book List */
ul {
  list-style: none;
  padding: 0;
}

li {
  display: flex;
  align-items: center;
  padding: 15px;
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 15px;
  transition: transform 0.2s;
}

li:hover {
  transform: translateY(-5px);
}

/* Book Cover */
.book-cover {
  width: 60px;
  height: 90px;
  border-radius: 4px;
  margin-right: 15px;
}

/* Book Title and Author */
strong {
  font-size: 1.1em;
  color: #333;
}

em {
  font-size: 0.9em;
  color: #777;
}

/* Stock Input and Button Container */
.stock-container {
  display: flex;
  align-items: center;
  margin-top: 10px;
}

.stock-input {
  width: 60px;
  padding: 5px;
  margin-left: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 0.9em;
}

/* Add Book Button */
.add_button {
  padding: 8px 12px;
  margin-top: 10px;
  background-color: #5cb85c;
  border: none;
  border-radius: 4px;
  color: #fff;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
}

.add_button:hover {
  background-color: #4cae4c;
}

/* Already Added Button */
.always-btn {
  background-color: #0275d8;
  cursor: default;
}

.always-btn:hover {
  background-color: #0275d8;
}

</style>
  