<template>
    <div id="logout">
        <button @click="handleLogout">Logout</button>
        <p v-if="errorMessage">{{ errorMessage }}</p>
    </div>
</template>
<script>
import { logout } from '@/services/authService';
// import { handleError } from 'vue';
export default {
    name: "UserLogout",
    data() {
        return {
            errorMessage: '',
        };
    },
    async handleLogout() {
            try{
                await logout();
                
                this.$router.push('login/');
            }catch (error){
                console.error('Logout Error:', error.message || error);
                this.errorMessage = error.response?.data?.detail || '失敗しました。';
            }
    },
}
</script>