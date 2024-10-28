import axios from "axios";
function getCSRFToken() {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; csrftoken=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
export async function  login(email, password) {
    try {
        const response = await axios.post('http://localhost:8000/api/auth/login/', 
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


export async function refreshToken() {
  try {
    const response = await axios.post('http://localhost:8000/api/auth/refresh/', {
      refresh: localStorage.getItem('refresh_token'),
    });

    // 新しいアクセストークンを保存
    localStorage.setItem('token', response.data.access);
    return response.data.access;
  } catch (error) {
    console.error('トークンのリフレッシュに失敗しました:', error);
    
    // トークンが無効な場合、ログアウト処理
    localStorage.removeItem('token');
    localStorage.removeItem('refresh_token');
    window.location.href = '/login';  // ログイン画面にリダイレクト
    throw error;
  }
}
export async function HelloWorld() {
  try {
    const response = await axios.get("http://localhost:8000/api/hello/", 
      {message},
      {
        headers: {
          'Content-Type': "application/json",
          'X-CSRFToken': getCSRFToken(),
        },
        withCredentials: true,
      },
    );
    console.log('APIの認証: ', response.data);
    return response.data;
  } catch(error) {
    console.error("APIの接続に失敗しました。", error.response);
    throw error;
  }
}
