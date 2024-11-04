<template>
    <div v-if="profile.name">
      <h2>Welcome to {{ profile.name }}</h2>
    </div>
  </template>
  
  <script>
  import { AccountProfile } from '@/services/apiService';
  export default {
    name: 'AccountProfile',  // 名前を変更
    props: ['name'],
    data(){
      return{
        profile: null,
        error: '',
      }
    },
    async created() {
      try{
        const response = await  AccountProfile(this.name);
        this.profile = response.data;
      }catch(error){
        this.error = "Failed to load book details. ";
        console.error("Profiel etails Error: ", error);
      }
    }
  };
  </script>
  