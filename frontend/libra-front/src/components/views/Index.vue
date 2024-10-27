<template>
    <div>
      <h2>API Message</h2>
      <p>{{ message }}</p>
    </div>
  </template>
  
  <script>
  export default {
    name: 'HomeIndex',  // 名前を変更
    date() {
      return{
        message: ""
      };
    },
    mounted() {
    axios.get('http://localhost:8000/api/hello/')
      .then(response => {
        this.message = response.data.message;
      })
      .catch(error => {
        console.error('APIエラー:', error);
      });
  },
  };

  </script>
  