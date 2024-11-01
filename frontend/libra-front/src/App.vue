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
</style>
