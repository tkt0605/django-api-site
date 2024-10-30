<template>
  <div>
    <h2>API Message</h2>
    <RouterLink to="/accounts/logout">Logout</RouterLink>
    <div class="seach_result">
      <ul>
        <li v-for="book in books" :key="book.id">
          <strong>{{ book.volumeInfo.title }}</strong> by
          <em>{{ book.volumeInfo.authors?.join(', ') }}</em>
        </li> 
      </ul>
    </div>
  </div>
</template>
  
<script>
export default{
  name: "HomeIndex",
}
</script>
  