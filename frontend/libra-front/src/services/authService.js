import axios from "axios";
function getCSRFToken() {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; csrftoken=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
export async function  login(email, password) {
    try {
        const response = await axios.post('http://localhost:8000/api/auth/login', 
            {email, password},
            {
                headers: {
                    'Content-Type': "application/json",
                    'X-CSRFToken': getCSRFToken(),
                },
                withCredentials: true,
            },
        );
        console.log("Login Success: ", response.data);
        return response.data;
    } catch (error) {
        console.error("Login Error: ", error.response);
        throw error
    }
}