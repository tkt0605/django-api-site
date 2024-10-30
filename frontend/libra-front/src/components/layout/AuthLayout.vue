<template>
    <div id="app">
        <!-- <h1>Libra</h1> -->
        <main id="main">
            <router-view /> 
        </main>
    </div>
</template>
<script>
export default {
    name: "AuthLayout",
};
</script>
<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Arial', sans-serif;
  }
  
  /* ページ全体の背景 */
  body {
    background-color: #f5f5f5;
    color: #333;
    line-height: 1.6;
  }
  
  /* アプリ全体のスタイル */
  #app {
    display: block;
    flex-direction: column;
    min-height: 100vh;
  }
  h1{
    text-align: center;
    margin: 50px auto;
  }
</style>