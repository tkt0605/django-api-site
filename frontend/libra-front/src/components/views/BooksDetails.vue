<template>
    <div>
        <ul>
            <div v-if="book">
                <h1>{{ book.title }}</h1>
                <img :src="book.image || 'https://via.placeholder.com/128x193?text=No+Cover'" alt="Book cover" />
                <p><strong>Author:</strong> {{ book.author }}</p>
                <p><strong>Publisher:</strong> {{ book.publisher }}</p>
                <p><strong>Published Date:</strong> {{ book.publish_date }}</p>
                <p><strong>ISBN-10:</strong> {{ book.isbn_10 }}</p>
                <p><strong>ISBN-13:</strong> {{ book.isbn_13 }}</p>
                <p><strong>Language:</strong> {{ book.language }}</p>
                <p><strong>Price:</strong> ${{ book.price }}</p>
            </div>
            <div v-else>
                <p>Loading book details...</p>
            </div>
        </ul>
    </div>
</template>

<script>
import { fetchBookDetail } from '@/services/apiService';
// import { create } from 'core-js/core/object';

export default{
    name: "fetchBookDetail",
    props: ["bookId"],
    data(){
        return{
            book: null,
            error: '',
        }
    },
    methods:{
        async created(){
            try{
                const response = await fetchBookDetail(this.bookId);
                this.book = response.data;
            }catch(error){
                this.error = 'Failed to load book details.';
                console.error("Book Details Error: ", error);
            }
        },
    },
};
</script>