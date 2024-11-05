<template>
  <router-view />  <!-- ここにルーティングの内容が表示される -->
</template>

<script>
// import IndexHome from './components/Index.vue';
export default {
  name: 'App',
  data() {
    return {
      // books: [],  // 初期化
      error: '',
      // query: '',
    };
  },
  async created() {
    await this.$store.dispatch('fetchUser');
  },
  // methods: {
  //     async search() {
  //       if (this.query) {
  //         this.$router.push({ name: 'SearchResult', query: { q: this.query } });
  //       }else {
  //         alert('検索クエリを入力してください。');
  //       }
  //     },
  //   },

}
</script>

<style>
/* Base Styling */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Roboto', sans-serif;
  background-color: #f9fafb;
  color: #333;
  line-height: 1.6;
}
</style>
