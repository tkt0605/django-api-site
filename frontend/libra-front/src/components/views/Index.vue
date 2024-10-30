<template>
  <div>
    <h2>API Message</h2>
    <RouterLink to="/accounts/logout">Logout</RouterLink>
  </div>
</template>
  
<script>
// export default{
//   name: "HomeIndex",
// }
export default {
    name: 'HomeIndex',
    data() {
      return{
        error: '',
        query: '',
        books: [],
      };
    },
    
    methods: {
      async search() {
        console.log(localStorage.getItem('token'));
        if (this.query) {
          this.$router.push({ name: 'SearchResult', query: { q: this.query } });
        }else {
          alert('検索クエリを入力してください。');
        }
      },
    },
  }
</script>
  