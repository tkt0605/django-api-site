<template>
    <div>
      <div v-if="error" class="error">{{ error }}</div>
  
      <div class="resault" v-if="books.length">
        <ul class='resalut-bar'>
          <div class='query'>検索結果： "{{ query }}"</div>
          <li class='books' v-for="book in books" :key="book.id">
            <router-link :to="{name: 'fetchBookDetail', params:{id: book.id}}">
                <img 
                :src="book.volumeInfo?.imageLinks?.thumbnail || book.volumeInfo?.imageLinks?.smallThumbnail" 
                alt="Book cover"
                class="book-cover"
                />
                <strong>{{ book.volumeInfo.title }}</strong> by<em>{{ book.volumeInfo.authors?.join(', ') }}</em>
            </router-link>
            <div class='add_button' v-if="isSuperUser">
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
/* Main Container */
.resault {
  margin-top: 20px;
  text-align: center;
}

/* Search Result Heading */
.query {
  font-size: 1.2em;
  font-weight: bold;
  color: #333;
  margin-bottom: 15px;
}

/* Error Message */
.error {
  color: #d9534f;
  font-size: 1em;
  margin-bottom: 15px;
  text-align: center;
}

/* Result List */
.resalut-bar {
  list-style-type: none;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  justify-content: center;
}

/* Individual Book Item */
.books {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  padding: 15px;
  width: 200px;
  text-align: center;
  transition: transform 0.3s;
}

.books:hover {
  transform: scale(1.05);
}

/* Book Cover Image */
.book-cover {
  width: 100px;
  height: 150px;
  border-radius: 5px;
  margin-bottom: 10px;
}

/* Book Title and Author */
.books strong {
  font-size: 1.1em;
  color: #333;
  display: block;
  margin: 8px 0;
}

.books em {
  font-size: 0.9em;
  color: #666;
  display: block;
  margin-bottom: 10px;
}

/* Add Button Container */
.add_button {
  margin-top: 10px;
}

/* Stock Input Container */
.stock-container {
  margin-bottom: 10px;
  text-align: left;
}

.stock-container label {
  font-size: 0.9em;
  font-weight: bold;
  color: #666;
  margin-right: 5px;
}

.stock-input {
  width: 60px;
  padding: 5px;
  border: 1px solid #ddd;
  border-radius: 5px;
  text-align: center;
}

/* Add Button */
.add_button button {
  background-color: #4a90e2;
  border: none;
  border-radius: 5px;
  color: #fff;
  font-weight: bold;
  cursor: pointer;
  padding: 8px 12px;
  transition: background-color 0.3s;
}

.add_button button:hover {
  background-color: #357ab9;
}

/* Already Added Button */
.always-btn {
  background-color: #c0c0c0;
  border: none;
  border-radius: 5px;
  color: #fff;
  font-weight: bold;
  padding: 8px 12px;
  cursor: not-allowed;
}

/* Responsive Adjustments */
@media (max-width: 480px) {
  .books {
    width: 100%;
    margin-bottom: 15px;
  }

  .book-cover {
    width: 80px;
    height: 120px;
  }
}

</style>
  